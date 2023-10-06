import os
from google.oauth2 import service_account
import vertexai
from vertexai.language_models import TextGenerationModel

dirname = os.path.dirname(__file__)
key_file_path = os.path.abspath(os.path.join(
    dirname, '..', '..', 'service_account_key.json'))
credentials = service_account.Credentials.from_service_account_file(
    key_file_path, scopes=['https://www.googleapis.com/auth/cloud-platform'])

parameters = {
    "max_output_tokens": 1024,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}

# https://cloud.google.com/vertex-ai/docs/generative-ai/text/test-text-prompts#generative-ai-test-text-prompt-python_vertex_ai_sdk
def predict(prompt: str) -> str:
    pass
