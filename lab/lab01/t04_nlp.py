import os
from typing import List
from google.cloud import language
from google.oauth2 import service_account


dirname = os.path.dirname(__file__)
key_file_path = os.path.abspath(os.path.join(
    dirname, '..', '..', 'service_account_key.json'))
credentials = service_account.Credentials.from_service_account_file(
    key_file_path)


def get_text_sentiment(text:str) -> str:
    pass


def get_text_entities(text:str) -> List:
    pass
