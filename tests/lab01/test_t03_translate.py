import os
from lab.lab01.t03_translate import detect_language, translate_to
from parameterized import parameterized
import unittest

dirname = os.path.dirname(__file__)
key_file_path = os.path.abspath(os.path.join(
    dirname, '..', '..', 'service_account_key.json'))

class TestOutput(unittest.TestCase):

    @parameterized.expand([
        ("雲端系統及數據中心管理高級文憑課程編號 IT114115", "zh-TW"),
        ("Higher Diploma in Cloud and Data Centre Administration Programme code IT114115", "en"),
        ("ワンピース", "ja"),
    ])
    def test_01_detect_language(self, text: str, expected_language_code: str):
        language_code = detect_language(text)
        self.assertEqual(expected_language_code, language_code)

    @parameterized.expand([
        ("雲端系統及數據中心管理高級文憑課程編號 IT114115", "en",
         'Higher Diploma in Cloud Systems and Data Center Management Course Number IT114115'),
        ("Higher Diploma in Cloud and Data Centre Administration Programme code IT114115",
         "ja", "クラウドおよびデータセンター管理上級ディプロマ プログラムコード IT114115"),
        ("ワンピース", "en", "one piece"),
    ])
    def test_02_translate_to(self, text: str, target_language_code: str, expected_translated_result: str):
        translated = translate_to(text, target_language_code)
        self.assertMultiLineEqual(expected_translated_result, translated)
