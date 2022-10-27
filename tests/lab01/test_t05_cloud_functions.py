import os
import random
import string
import sys
import unittest

from config import LOCATIONS, PROJECT_ID, STUDENT_ID
from google.api_core import exceptions
from lab.lab01.t05_cloud_functions import (check_cloud_function_state,
                                           create_function,
                                           invoke_cloud_function_state)

sys.path.append("...")

dirname = os.path.dirname(__file__)
key_file_path = os.path.join(dirname, '..', '..', 'service_account_key.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file_path
os.environ["PROJECT_ID"] = PROJECT_ID
os.environ["LOCATIONS"] = LOCATIONS
os.environ["STUDENT_ID"] = STUDENT_ID

bucket_name = STUDENT_ID + "-ivestudent"


class TestOutput(unittest.TestCase):

    def test_01_create_function(self):
        try:
            create_function(bucket_name)
        except exceptions.AlreadyExists:
            print("Function exists.")

    def test_02_check_cloud_function_state_active(self):
        state = check_cloud_function_state()
        self.assertEqual("ACTIVE", state)

    def test_03_invoke_cloud_function_state(self):
        name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        state = invoke_cloud_function_state(name)
        self.assertEqual(f"Hello {name}!", state)
