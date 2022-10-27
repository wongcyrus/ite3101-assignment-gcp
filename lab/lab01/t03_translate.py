from google.cloud import translate
from os import environ

# Refernece 
# https://codelabs.developers.google.com/codelabs/cloud-translation-python3#0

def get_parent():
    project_id = environ.get("PROJECT_ID", "")
    parent = f"projects/{project_id}"
    return parent

def detect_language(text):
    pass

def translate_to(text:str, target_language_code:str):
    pass