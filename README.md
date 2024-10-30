<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
AI-Powered-Request-Handler-Service
</h1>
<h4 align="center">A Python backend service that simplifies interacting with OpenAI's language models.</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-blue" alt="Framework used">
  <img src="https://img.shields.io/badge/Language-Python-red" alt="Programming language">
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue" alt="Database used">
  <img src="https://img.shields.io/badge/API-OpenAI-black" alt="API used">
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/AI-Powered-Request-Handler-Service?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/AI-Powered-Request-Handler-Service?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/AI-Powered-Request-Handler-Service?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 License
- 👏 Authors

## 📍 Overview

This repository contains an AI Powered Request Handler Service, a Python backend service designed to simplify the interaction with OpenAI's language models. This service empowers developers to effortlessly integrate AI capabilities into their applications without directly handling OpenAI's APIs.

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular architectural pattern with separate directories for different functionalities, ensuring easier maintenance and scalability.             |
| 📄 | **Documentation**  | The repository includes a README file that provides a detailed overview of the service, its dependencies, and usage instructions.|
| 🔗 | **Dependencies**   | The codebase relies on various external libraries and packages such as `FastAPI`, `uvicorn`, `openai`, `sqlalchemy`, `psycopg2-binary`, `python-dotenv`, and `PyJWT`, which are essential for building the API, interacting with the database, and handling authentication.|
| 🧩 | **Modularity**     | The modular structure allows for easier maintenance and reusability of the code, with separate directories and files for different functionalities such as routes, services, and models.|
| 🧪 | **Testing**        | Includes unit tests using `pytest` to ensure the reliability and robustness of the codebase.       |
| ⚡️  | **Performance**    |  The performance of the service can be optimized by using caching mechanisms and asynchronous processing. |
| 🔐 | **Security**       | Enhances security by implementing measures such as input validation, API key management, and JWT authentication.|
| 🔀 | **Version Control**| Utilizes Git for version control with a `startup.sh` script for automated deployment processes.|
| 🔌 | **Integrations**   | Interacts with OpenAI's API for text generation and includes a PostgreSQL database (optional) for data storage.|
| 📶 | **Scalability**    |  The service is designed to handle increased user load and data volume, utilizing asynchronous processing and database optimization for better scalability.           |

## 📂 Structure
```text
AI-Powered-Request-Handler-Service/
├── src/
│   ├── main.py
│   ├── routes/
│   │   └── request_routes.py
│   ├── services/
│   │   └── request_service.py
│   └── models/
│       └── request.py
├── .env
├── tests/
│   └── test_request_service.py
├── startup.sh
└── requirements.txt
```

## 💻 Installation

### 🔧 Prerequisites
- Python 3.9+
- PostgreSQL 15+ (optional)
- Docker (optional)

### 🚀 Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/coslynx/AI-Powered-Request-Handler-Service.git
   cd AI-Powered-Request-Handler-Service
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
   # Create a database (optional):
   createdb your_database_name
   # Set the database URL in the .env file:
   DATABASE_URL=postgresql://user:password@host:port/your_database_name
   ```
4. Configure environment variables:
   ```bash
   cp .env.example .env
   # Fill in the OPENAI_API_KEY and DATABASE_URL (if using a database)
   ```
5. (Optional) Build the Docker image:
   ```bash
   docker build -t ai-request-handler .
   ```
6. (Optional) Run the application using Docker:
   ```bash
   docker run -p 8000:8000 ai-request-handler
   ```

## 🏗️ Usage
### 🏃‍♂️ Running the MVP
1. Start the API server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
2. Access the API endpoint:
   - Send a POST request to `http://localhost:8000/request` with the following JSON body:
     ```json
     {
       "prompt": "This is a text prompt for the OpenAI model."
     }
     ```
   - The response will contain the AI-generated text.

## 🌐 Hosting
### 🚀 Deployment Instructions

#### Deploying to Heroku (optional)
1. Install the Heroku CLI:
   ```bash
   npm install -g heroku
   ```
2. Login to Heroku:
   ```bash
   heroku login
   ```
3. Create a new Heroku app:
   ```bash
   heroku create ai-request-handler-production
   ```
4. Set up environment variables:
   ```bash
   heroku config:set OPENAI_API_KEY=your_api_key
   heroku config:set DATABASE_URL=your_database_url_here
   ```
5. Deploy the code:
   ```bash
   git push heroku main
   ```

#### Deploying using Docker (optional)
1. Build the Docker image:
   ```bash
   docker build -t ai-request-handler .
   ```
2. Push the image to a Docker registry:
   ```bash
   docker push your_docker_registry/ai-request-handler:latest
   ```
3. Deploy the image to your chosen cloud platform (e.g., AWS ECS, Google Kubernetes Engine):
   - Follow the deployment instructions for your chosen platform, referencing the Docker image name and tag.

### 🔑 Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required).
- `DATABASE_URL`: Connection string for the PostgreSQL database (optional, if using a database).

## 📜 API Documentation

### 🔍 Endpoints

- **POST /request**
  - Description: Handles user requests and sends them to the OpenAI API.
  - Request Body:
    ```json
    {
      "prompt": "Your text prompt here."
    }
    ```
  - Response Body:
    ```json
    {
      "text": "AI-generated text based on the prompt."
    }
    ```

## 📜 License & Attribution

### 📄 License
This Minimum Viable Product (MVP) is licensed under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) license.

### 🤖 AI-Generated MVP
This MVP was entirely generated using artificial intelligence through [CosLynx.com](https://coslynx.com).

No human was directly involved in the coding process of the repository: AI-Powered-Request-Handler-Service

### 📞 Contact
For any questions or concerns regarding this AI-generated MVP, please contact CosLynx at:
- Website: [CosLynx.com](https://coslynx.com)
- Twitter: [@CosLynxAI](https://x.com/CosLynxAI)

<p align="center">
  <h1 align="center">🌐 CosLynx.com</h1>
</p>
<p align="center">
  <em>Create Your Custom MVP in Minutes With CosLynxAI!</em>
</p>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Developers-Drix10,_Kais_Radwan-red" alt="">
  <img src="https://img.shields.io/badge/Website-CosLynx.com-blue" alt="">
  <img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="">
  <img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4,_v6-black" alt="">
</div>