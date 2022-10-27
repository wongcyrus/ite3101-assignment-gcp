import os

from google.cloud import exceptions, storage

dirname = os.path.dirname(__file__)
key_file_path = os.path.join(dirname, '..', '..', 'service_account_key.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file_path

# Reference to this sample code
# https://cloud.google.com/storage/docs/hosting-static-website#storage-create-bucket-code_samples


def create_static_website_cloud_storage_bucket_if_not_exit(prefix: str):    
    bucket_name = prefix + "-ivestudent"
    pass

def upload_text_to_bucket(bucket_name: str, path_name: str, content: str, content_type: str = "text/html"):
    pass

def upload_file_to_bucket(bucket_name: str, path_name: str, source_file_name: str, content_type: str = "image/jpeg"):
    pass

def upload_index_and_404_pages(bucket_name: str):
    pass


def upload_html_file_to_bucket(bucket_name: str, path: str, repeat: int):
    pass


def delete_text_html_to_bucket(bucket_name: str, path: str, repeat: int):
    pass
