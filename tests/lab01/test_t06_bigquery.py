from time import sleep
import unittest
from google.cloud import bigquery
from config import PROJECT_ID

from lab.lab01.t06_bigquery import create_dataset_if_not_exist, create_table_if_not_exist, delete_table, insert_data, get_all_rows


class TestOutput(unittest.TestCase):

    def test_01_create_dataset_if_not_exist(self):
        create_dataset_if_not_exist()
        client = bigquery.Client()
        dataset_id = f"{PROJECT_ID}.ive_dataset"
        client.get_dataset(dataset_id)

    def test_02_create_table_if_not_exist(self):
        delete_table()
        create_table_if_not_exist()
        client = bigquery.Client()
        table_id = f"{PROJECT_ID}.ive_dataset.students"      
        client.get_table(table_id)
        

    # This test may not pass immediately after test_02_create_table_if_not_exist, as it takes time to create the table!
    def test_03_insert_data_and_get_all_rows(self):
        rows = get_all_rows()
        count = len(rows)
        rows_to_insert = [
            {"first_name": "Phred", "last_name": "Phlyntstone", "age": 10},
            {"first_name": "Wylma", "last_name": "Phlyntstone", "age": 11},
        ]
        insert_data(rows_to_insert)
        rows = get_all_rows()
        self.assertEqual(count + 2, len(rows))
