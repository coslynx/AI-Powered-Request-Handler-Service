from typing import Dict, Any
import openai
from dotenv import load_dotenv
import os

load_dotenv()

class RequestService:
    """
    Service for handling requests to OpenAI API.
    """

    def __init__(self):
        """
        Initializes the OpenAI API client.
        """
        self.openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_text(self, prompt: str, model: str = "text-davinci-003", max_tokens: int = 1000, temperature: float = 0.7) -> Dict[str, Any]:
        """
        Generates text using the OpenAI API.

        Args:
            prompt: The text prompt to be used for text generation.
            model: The OpenAI model to use for text generation.
            max_tokens: The maximum number of tokens to generate.
            temperature: The temperature parameter for controlling the creativity of the generated text.

        Returns:
            A dictionary containing the generated text and other information.

        Raises:
            openai.error.APIError: If an error occurs while calling the OpenAI API.
        """
        try:
            response = self.openai_client.completions.create(
                model=model,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response.choices[0].text
        except openai.error.APIError as e:
            raise HTTPException(status_code=500, detail=f"OpenAI API Error: {e}")