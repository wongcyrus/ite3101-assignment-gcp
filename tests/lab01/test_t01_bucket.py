import os
from time import sleep
import unittest
from datetime import datetime

import requests
from config import STUDENT_ID
from google.cloud import storage
from lab.lab01.t01_bucket import (
    create_static_website_cloud_storage_bucket_if_not_exit,
    delete_text_html_to_bucket, upload_html_file_to_bucket,
    upload_index_and_404_pages)
from google.oauth2 import service_account


PREFIX = "" if os.environ.get('PREFIX') is None else os.environ.get('PREFIX')

dirname = os.path.dirname(__file__)
key_file_path = os.path.abspath(os.path.join(
    dirname, '..', '..', 'service_account_key.json'))
credentials = service_account.Credentials.from_service_account_file(
    key_file_path)
bucket_name = f'{PREFIX}{STUDENT_ID}'


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.random_str = datetime.now().strftime('%Y/%m/%d')

    def test_create_static_website_cloud_storage_bucket_if_not_exit(self):
        storage_client = storage.Client(credentials=credentials)
        create_static_website_cloud_storage_bucket_if_not_exit(bucket_name)
        bucket = storage_client.get_bucket(bucket_name)
        policy = bucket.get_iam_policy()

        self.assertIn({"role": "roles/storage.objectViewer",
                      "members": {'allUsers'}}, policy.bindings)

    def test_upload_index_and_404_pages(self):
        storage_client = storage.Client(credentials=credentials)
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob("index.html")
        if blob.exists():
            blob.delete()
        blob = bucket.blob("404.html")
        if blob.exists():
            blob.delete()

        upload_index_and_404_pages(bucket_name)
        index = '''
<!DOCTYPE html>
<html>
<head>
<title>Index</title>
</head>
<body>
<h1>Index Page</h1>
</body>
</html>     
'''

        page404 = '''
<!DOCTYPE html>
<html>
<head>
<title>Not Found</title>
</head>
<body>
<h1>Not Found</h1>
</body>
</html>     
'''
        index_url = f"https://storage.googleapis.com/{bucket_name}/index.html"
        response = requests.get(url=index_url, timeout=10)
        self.assertEqual(response.text, index)
        page404_url = f"https://storage.googleapis.com/{bucket_name}/404.html"
        response = requests.get(url=page404_url, timeout=10)
        self.assertEqual(response.text, page404)

    def test_upload_html_file_to_bucket(self):
        upload_html_file_to_bucket(bucket_name, self.random_str, 4)
        for i in range(4):
            content = f'''
<!DOCTYPE html>
<html>
<head>
<title>Index</title>
</head>
<body>
<h1>{i}</h1>
</body>
</html>     
'''
            url = f"https://storage.googleapis.com/{bucket_name}/{self.random_str}/{i}.html"
            response = requests.get(url=url, timeout=10)
            self.assertEqual(response.text, content)

    def test_delete_text_html_to_bucket(self):
        delete_text_html_to_bucket(bucket_name, self.random_str, 4)
        # Delete is in Eventually Consistency and needs to wait for a few seconds.
        sleep(5)

        storage_client = storage.Client(credentials=credentials)
        create_static_website_cloud_storage_bucket_if_not_exit(bucket_name)
        bucket = storage_client.get_bucket(bucket_name)

        for i in range(4):
            blob = bucket.blob(f"{self.random_str}/{i}.html")
            self.assertNotIn(blob, bucket.list_blobs())
        # It should not have error if files are not exist!
        delete_text_html_to_bucket(bucket_name, self.random_str, 4)


if __name__ == '__main__':
    unittest.main()
