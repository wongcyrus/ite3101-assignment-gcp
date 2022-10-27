import os
from google.cloud import bigquery
from google.cloud.exceptions import NotFound

from config import PROJECT_ID


dirname = os.path.dirname(__file__)
key_file_path = os.path.join(dirname, '..', '..', 'service_account_key.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file_path

# https://cloud.google.com/bigquery/docs/samples/bigquery-dataset-exists
# https://cloud.google.com/bigquery/docs/samples/bigquery-create-dataset


def create_dataset_if_not_exist():
    client = bigquery.Client()
    dataset_id = f"{PROJECT_ID}.ive_dataset"
    pass


# https://cloud.google.com/bigquery/docs/samples/bigquery-delete-table
def delete_table():
    pass

# https://cloud.google.com/bigquery/docs/samples/bigquery-table-exists
# https://cloud.google.com/bigquery/docs/samples/bigquery-create-table
# https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#TableFieldSchema.FIELDS.type
def create_table_if_not_exist():
    pass

# https://cloud.google.com/bigquery/docs/samples/bigquery-table-insert-rows-explicit-none-insert-ids
# REMARK: The example has bug and you need to think about how to modify it! That is something very common at work!
def insert_data(rows_to_insert):
    pass

 

# https://cloud.google.com/bigquery/docs/samples/bigquery-query
def get_all_rows():
    pass
