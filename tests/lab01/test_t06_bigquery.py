import os
import unittest
from google.cloud import bigquery
from google.oauth2 import service_account
from config import STUDENT_ID

from lab.lab01.t06_bigquery import create_dataset_if_not_exist, create_table_if_not_exist, delete_table, insert_data, get_all_rows

PREFIX = "" if os.environ.get('PREFIX') is None else os.environ.get('PREFIX')
dirname = os.path.dirname(__file__)
key_file_path = os.path.join(dirname, '..', '..', 'service_account_key.json')
credentials = service_account.Credentials.from_service_account_file(
    key_file_path)

PREFIX = PREFIX + STUDENT_ID


class TestOutput(unittest.TestCase):

    def test_01_create_dataset_if_not_exist(self):
        create_dataset_if_not_exist(PREFIX)
        client = bigquery.Client(credentials=credentials)
        dataset_id = f"{credentials.project_id}.{PREFIX}ive_dataset"
        client.get_dataset(dataset_id)

    def test_02_create_table_if_not_exist(self):
        delete_table(PREFIX)
        create_table_if_not_exist(PREFIX)
        client = bigquery.Client(credentials=credentials)
        table_id = f"{credentials.project_id}.{PREFIX}ive_dataset.students"
        client.get_table(table_id)

    # This test may not pass immediately after test_02_create_table_if_not_exist, as it takes time to create the table!
    def test_03_insert_data_and_get_all_rows(self):
        rows = get_all_rows(PREFIX)
        count = len(rows)
        rows_to_insert = [
            {"first_name": "Phred", "last_name": "Phlyntstone", "age": 10},
            {"first_name": "Wylma", "last_name": "Phlyntstone", "age": 11},
        ]
        insert_data(rows_to_insert, PREFIX)
        rows = get_all_rows(PREFIX)
        self.assertEqual(count + 2, len(rows))
