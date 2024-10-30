from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv
import os

from .routes import router  # Import the API routes module

load_dotenv()  # Load environment variables from .env

app = FastAPI()  # Create the FastAPI application instance

# Enable CORS (Cross-Origin Resource Sharing) for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include the router to define API routes
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Start the API server