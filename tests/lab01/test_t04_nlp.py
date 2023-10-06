from parameterized import parameterized
from lab.lab01.t04_nlp import get_text_sentiment, get_text_entities
import unittest


class TestOutput(unittest.TestCase):

    @parameterized.expand([
        ("My dog is death! I feel heart breaking!", "Clearly Negative"),
        ("Great! I won a game and get a free ticket to Ocean Park", "Clearly Positive"),
        ("I don't know that is good or not to resign from my current job!", "Mixed"),
        ("Good moring! How are you?", "Neutral")
    ])
    def test_01_detect_language(self, text: str, expected_sentiment: str):
        sentiment = get_text_sentiment(text)
        self.assertEqual(expected_sentiment, sentiment)

    def test_02_get_text_entities(self):
        result = get_text_entities(
            "IVE Higher Diploma in Cloud and Data Centre Administration is good!")
        expected_result = [
            {'mid': '-', 'name': 'IVE Higher Diploma', 'salience': '55.9%',
                'type': 'PERSON', 'wikipedia_url': '-'},
            {'mid': '/m/02y_9m3', 'name': 'Cloud', 'salience': '33.3%', 'type': 'OTHER',
                'wikipedia_url': 'https://en.wikipedia.org/wiki/Cloud_computing'},
            {'mid': '-', 'name': 'Data Centre Administration',
                'salience': '10.8%', 'type': 'ORGANIZATION', 'wikipedia_url': '-'}
        ]
        self.assertCountEqual(expected_result, result)
