import os

from google.cloud import exceptions, storage
from google.oauth2 import service_account

key_file_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'service_account_key.json'))
credentials = service_account.Credentials.from_service_account_file(
    key_file_path)

# Reference to this sample code
# https://cloud.google.com/storage/docs/hosting-static-website#storage-create-bucket-code_samples


def create_static_website_cloud_storage_bucket_if_not_exit(bucket_name: str):       
    pass

def upload_text_to_bucket(bucket_name: str, path_name: str, content: str, content_type: str = "text/html"):
    pass

def upload_file_to_bucket(bucket_name: str, path_name: str, source_file_name: str, content_type: str = "image/jpeg"):
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(path_name)
    blob.upload_from_filename(source_file_name, content_type=content_type)

def upload_index_and_404_pages(bucket_name: str):
    pass


def upload_html_file_to_bucket(bucket_name: str, path: str, repeat: int):
    pass


def delete_text_html_to_bucket(bucket_name: str, path: str, repeat: int):
    pass
