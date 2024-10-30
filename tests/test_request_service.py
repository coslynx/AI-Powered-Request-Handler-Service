import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.services.request_service import RequestService
from unittest.mock import patch
from src.models.request import RequestPayload
import openai

client = TestClient(app)

@pytest.fixture
def request_service():
    return RequestService()

def test_generate_text_success(request_service):
    with patch.object(openai.OpenAI, 'completions', autospec=True) as mock_completions:
        mock_completions.create.return_value = {
            'choices': [{'text': 'This is a test response.'}]
        }
        prompt = 'This is a test prompt.'
        response = request_service.generate_text(prompt)
        assert response == 'This is a test response.'
        mock_completions.create.assert_called_once_with(
            model='text-davinci-003',
            prompt=prompt,
            max_tokens=1000,
            temperature=0.7
        )

def test_generate_text_api_error(request_service):
    with patch.object(openai.OpenAI, 'completions', autospec=True) as mock_completions:
        mock_completions.create.side_effect = openai.error.APIError('API error')
        with pytest.raises(openai.error.APIError):
            request_service.generate_text('This is a test prompt.')

def test_handle_request_success(request_service):
    with patch.object(request_service, 'generate_text', autospec=True) as mock_generate_text:
        mock_generate_text.return_value = 'This is a test response.'
        response = client.post('/request', json={'prompt': 'This is a test prompt.'})
        assert response.status_code == 200
        assert response.json() == 'This is a test response.'
        mock_generate_text.assert_called_once_with(prompt='This is a test prompt.')

def test_handle_request_invalid_prompt(request_service):
    response = client.post('/request', json={'prompt': 'A' * 1001})
    assert response.status_code == 422

def test_handle_request_api_error(request_service):
    with patch.object(request_service, 'generate_text', autospec=True) as mock_generate_text:
        mock_generate_text.side_effect = openai.error.APIError('API error')
        response = client.post('/request', json={'prompt': 'This is a test prompt.'})
        assert response.status_code == 500

def test_handle_request_authentication_error(request_service):
    with patch.object(openai.OpenAI, 'completions', autospec=True) as mock_completions:
        mock_completions.create.return_value = {
            'choices': [{'text': 'This is a test response.'}]
        }
        response = client.post('/request', json={'prompt': 'This is a test prompt.'}, headers={'Authorization': 'Bearer invalid_token'})
        assert response.status_code == 401