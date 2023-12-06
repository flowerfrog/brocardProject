import json
import os
from dotenv import load_dotenv
resources_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../schema'))


def load_schema(filepath):
    with open(os.path.join(resources_path, filepath)) as file:
        schema = json.load(file)
        return schema


def load_env():
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    return API_KEY
