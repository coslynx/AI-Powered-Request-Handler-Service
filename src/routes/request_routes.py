from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, validator
import openai
import jwt
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

router = APIRouter()

class RequestPayload(BaseModel):
    prompt: str

    @validator("prompt")
    def prompt_validation(cls, value):
        if len(value) > 1000:
            raise ValueError("Prompt cannot exceed 1000 characters.")
        return value

@router.post("/request")
async def handle_request(payload: RequestPayload, request: Request):
    """
    Handles user requests, validates input, sends to OpenAI API, and returns the response.

    Args:
        payload: The user's request payload containing the text prompt.
        request: The FastAPI Request object, used for authentication.

    Returns:
        JSONResponse: The AI-generated response from OpenAI.

    Raises:
        HTTPException:  For invalid input or authentication errors.
    """
    try:
        # Authentication (if applicable)
        auth_header = request.headers.get("Authorization")
        if auth_header:
            token = auth_header.split(" ")[1]
            decoded_token = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
            # ... (Process token and proceed with request)
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")

        # Send request to OpenAI API
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=payload.prompt,
            max_tokens=1000,
            temperature=0.7,
        )

        # Format and return response
        return JSONResponse(response.choices[0].text)

    except openai.error.APIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API Error: {e}")
    except jwt.exceptions.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail=f"Invalid authentication token: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")