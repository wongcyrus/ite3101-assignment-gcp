import os
import sys
import unittest
from google.api_core import exceptions
from config import LOCATIONS, STUDENT_ID

from lab.lab01.t05_cloud_functions import (check_cloud_function_state,
                                           create_function)

sys.path.append("...")

PREFIX = "" if os.environ.get('PREFIX') is None else os.environ.get('PREFIX')
dirname = os.path.dirname(__file__)
key_file_path = os.path.abspath(os.path.join(
    dirname, '..', '..', 'service_account_key.json'))

os.environ["LOCATIONS"] = LOCATIONS

bucket_name = PREFIX + STUDENT_ID
function_id = "fn" + PREFIX + STUDENT_ID + "-ivefunction"


class TestOutput(unittest.TestCase):

    def test_01_create_function(self):
        try:
            create_function(bucket_name, function_id)
        except exceptions.AlreadyExists:
            print("Function exists.")

    def test_02_check_cloud_function_state_active_or_deploying(self):
        state = check_cloud_function_state(function_id)
        self.assertIn(state,["DEPLOYING","ACTIVE"])
