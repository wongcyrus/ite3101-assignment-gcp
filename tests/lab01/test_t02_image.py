
import os
import sys
import unittest
from google.cloud import storage
from config import STUDENT_ID
from lab.lab01.t02_image import count_dog_and_cat, get_text_from_image, get_emotional_index
from parameterized import parameterized

sys.path.append("...")


dirname = os.path.dirname(__file__)
key_file_path = os.path.join(dirname, '..', '..', 'service_account_key.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file_path

bucket_name = STUDENT_ID + "-ivestudent"


class TestOutput(unittest.TestCase):

    @parameterized.expand([
        ('dogs.jpg', 4, 0),
        ('cats.jpg', 0, 2),
        ('dogsandcats.jpg', 3, 1),
    ])
    def test_01_count_dog_and_cat(self, image: str, dogs: int, cats: int):
        dirname = os.path.dirname(__file__)
        file_path_name = os.path.join(dirname, 'images', image)
        dog_count, cat_count = count_dog_and_cat(
            bucket_name, file_path_name, 0.7)
        self.assertEqual(dog_count, dogs)
        self.assertEqual(cat_count, cats)

        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)

        blob = bucket.blob(f"images/{image}")
        self.assertTrue(blob.exists())

    def test_02_get_text_from_image(self):
        dirname = os.path.dirname(__file__)
        file_path_name = os.path.join(dirname, 'images', "iveIT.png")
        text = get_text_from_image(bucket_name, file_path_name)
        self.assertEqual(
            "IVE\nInformation Technology\nMember of VTC Group", text)

    @parameterized.expand([
        ('happy-class.jpg', 12),
        ('unhappy-class.jpg', 6)
    ])
    def test_03_get_emotional_index(self, image: str, expected_emotional_index: float):
        dirname = os.path.dirname(__file__)
        file_path_name = os.path.join(dirname, 'images', image)
        emotional_index = get_emotional_index(bucket_name, file_path_name)
        self.assertAlmostEqual(expected_emotional_index, emotional_index, 10)
