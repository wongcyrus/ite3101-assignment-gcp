import os
from os import environ
from google.cloud import translate
from google.oauth2 import service_account


dirname = os.path.dirname(__file__)
key_file_path = os.path.abspath(os.path.join(
    dirname, '..', '..', 'service_account_key.json'))
credentials = service_account.Credentials.from_service_account_file(
    key_file_path)
# Reference
# https://codelabs.developers.google.com/codelabs/cloud-translation-python3#0


def get_parent() -> str:
    parent = f"projects/{credentials.project_id}"
    return parent


def detect_language(text:str) -> str:
    pass

def translate_to(text:str, target_language_code:str) -> str:
    pass