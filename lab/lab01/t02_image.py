import os
from google.cloud import vision
from google.oauth2 import service_account
from lab.lab01.t01_bucket import upload_file_to_bucket


key_file_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'service_account_key.json'))
credentials = service_account.Credentials.from_service_account_file(
    key_file_path)


# Reference https://codelabs.developers.google.com/codelabs/cloud-vision-api-python#0


def prepare_image(bucket_name: str, image_file_path: str) -> vision.Image:
    pass


def count_dog_and_cat(bucket_name: str, image_file_path: str, score: float) -> (int, int):
    image = prepare_image(bucket_name, image_file_path)
    pass


def get_text_from_image(bucket_name: str, image_file_path: str) -> str:
    image = prepare_image(bucket_name, image_file_path)
    pass


def get_emotional_index(bucket_name: str, image_file_path: str) -> int:
    image = prepare_image(bucket_name, image_file_path)
    pass
