#!/bin/bash

set -euo pipefail

export OPENAI_API_KEY="${OPENAI_API_KEY}"
export DATABASE_URL="${DATABASE_URL}"

log_info() {
  echo "$(date +"%Y-%m-%d %H:%M:%S") - $1"
}

log_error() {
  echo "$(date +"%Y-%m-%d %H:%M:%S") - ERROR: $1" >&2
}

cleanup() {
  log_info "Cleaning up..."
  rm -f /var/run/ai-request-handler.pid 2>/dev/null
}

check_dependencies() {
  log_info "Checking dependencies..."
  which uvicorn > /dev/null 2>&1
  which python > /dev/null 2>&1
}

start_backend() {
  log_info "Starting backend service..."
  nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
  store_pid $!
  wait_for_service "localhost:8000" 5 10
  verify_service "localhost:8000" 3
}

store_pid() {
  echo "$1" > /var/run/ai-request-handler.pid
}

wait_for_service() {
  local host="$1"
  local port="$2"
  local timeout="$3"
  local interval="$4"
  local attempts=0
  while [[ $attempts -lt $timeout ]]; do
    if nc -z "$host" "$port" > /dev/null 2>&1; then
      log_info "Service is ready on $host:$port."
      return 0
    fi
    attempts=$((attempts + 1))
    log_info "Waiting for service on $host:$port..."
    sleep $interval
  done
  log_error "Timeout waiting for service on $host:$port."
  exit 1
}

verify_service() {
  local host="$1"
  local port="$2"
  local attempts=0
  while [[ $attempts -lt $timeout ]]; do
    if curl -s -o /dev/null -w "%{http_code}" "$host:$port/health" | grep -q 200; then
      log_info "Service health check passed."
      return 0
    fi
    attempts=$((attempts + 1))
    log_info "Waiting for service health check on $host:$port..."
    sleep $interval
  done
  log_error "Timeout waiting for service health check on $host:$port."
  exit 1
}

check_dependencies
start_backend

trap cleanup EXIT ERR

log_info "Startup complete."