from pydantic import BaseModel, validator
from typing import Optional

class RequestPayload(BaseModel):
    prompt: str
    model: Optional[str] = "text-davinci-003"
    max_tokens: Optional[int] = 1000
    temperature: Optional[float] = 0.7

    @validator("prompt")
    def prompt_validation(cls, value):
        if len(value) > 1000:
            raise ValueError("Prompt cannot exceed 1000 characters.")
        return value

    @validator("model")
    def model_validation(cls, value):
        if value not in ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"]:
            raise ValueError("Invalid model name. Allowed models: text-davinci-003, text-curie-001, text-babbage-001, text-ada-001")
        return value

    @validator("max_tokens")
    def max_tokens_validation(cls, value):
        if value <= 0:
            raise ValueError("Max tokens must be a positive integer.")
        return value

    @validator("temperature")
    def temperature_validation(cls, value):
        if value < 0 or value > 1:
            raise ValueError("Temperature must be between 0 and 1.")
        return value