import datetime
import os
import sys
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

sys.path.append("...")


dirname = os.path.dirname(__file__)
key_file_path = os.path.join(dirname, '..', '..', 'service_account_key.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file_path
bucket_name = STUDENT_ID + "-ivestudent"


class TestOutput(unittest.TestCase):

    def setup_method(self, test_method):
        self.random_str = datetime.now().strftime('%Y/%m/%d')

    def test_01_create_static_website_cloud_storage_bucket_if_not_exit(self):
        storage_client = storage.Client()
        create_static_website_cloud_storage_bucket_if_not_exit(STUDENT_ID)
        bucket = storage_client.get_bucket(bucket_name)
        policy = bucket.get_iam_policy()

        for p in policy.bindings:
            if (p['role'] == "roles/storage.objectViewer"):
                m = p['members']
                self.assertSetEqual(m, {"allUsers"})

    def test_02_upload_index_and_404_pages(self):
        storage_client = storage.Client()
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
        index_url = f"https://storage.googleapis.com/{STUDENT_ID}-ivestudent/index.html"
        r = requests.get(url=index_url)
        self.assertEqual(r.text, index)
        page404_url = f"https://storage.googleapis.com/{STUDENT_ID}-ivestudent/404.html"
        r = requests.get(url=page404_url)
        self.assertEqual(r.text, page404)

    def test_03_upload_html_file_to_bucket(self):
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
            url = f"https://storage.googleapis.com/{STUDENT_ID}-ivestudent/{self.random_str}/{i}.html"
            r = requests.get(url=url)
            self.assertEqual(r.text, content)

    def test_04_delete_text_html_to_bucket(self):
        delete_text_html_to_bucket(bucket_name, self.random_str, 4)
        # Delete is in Eventually Consistency and needs to wait for a few seconds.
        sleep(5)

        storage_client = storage.Client()
        create_static_website_cloud_storage_bucket_if_not_exit(STUDENT_ID)
        bucket = storage_client.get_bucket(bucket_name)

        for i in range(4):
            blob = bucket.blob(f"{self.random_str}/{i}.html")
            self.assertFalse(blob.exists())
        # It should not have error if files are not exist!
        delete_text_html_to_bucket(bucket_name, self.random_str, 4)


if __name__ == '__main__':
    unittest.main()
