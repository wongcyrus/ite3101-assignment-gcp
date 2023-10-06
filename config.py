import os

STUDENT_ID = "979785543131" if os.environ.get(
    'STUDENT_ID') is None else os.environ.get('STUDENT_ID')
API_KEY = "AIzaSyBzy23jbCFZ5IhHtxSShRl7GI-iRg2DVxU"

API_ENDPOINT = 'https://gateway-8eur6cwg.ue.gateway.dev'
LOCATIONS = "asia-east2"
