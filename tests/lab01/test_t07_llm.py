import os
from lab.lab01.t07_llm import predict
from parameterized import parameterized
import unittest

dirname = os.path.dirname(__file__)
key_file_path = os.path.abspath(os.path.join(
    dirname, '..', '..', 'service_account_key.json'))

class TestOutput(unittest.TestCase):

    @parameterized.expand([
        ("What is the color of apple?", "red"),
        ("What is the color of banana?", "yellow"),
        ("3 - 2 = ", "1"),
        ("Write Python code print out 'Hello World!' ", "print("),
    ])
    def test_01_predict(self, text: str, expected: str):
        answer = predict(text)
        self.assertTrue(expected in answer.lower())