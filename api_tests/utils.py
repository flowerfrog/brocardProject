import os
from dotenv import load_dotenv
import json
import requests
from allure_commons.types import AttachmentType
import logging
import allure

resources_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../schema'))


def load_schema(filepath):
    with open(os.path.join(resources_path, filepath)) as file:
        schema = json.load(file)
        return schema


def load_env():
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    return API_KEY


def brocard_api_get(url, **kwargs):
    with allure.step("API Request"):
        result = requests.get(url="https://private.mybrocard.com/api/v2" + url, **kwargs)
        allure.attach(body=result.request.method + " " + result.request.url, name="Request URL", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)
        return result


def brocard_api_post(url, **kwargs):
    with allure.step("API Request"):
        result = requests.post(url="https://private.mybrocard.com/api/v2" + url, **kwargs)
        allure.attach(body=result.request.method + " " + result.request.url, name="Request URL", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)
        return result


def brocard_api_put(url, **kwargs):
    with allure.step("API Request"):
        result = requests.put(url="https://private.mybrocard.com/api/v2" + url, **kwargs)
        allure.attach(body=result.request.method + " " + result.request.url, name="Request URL", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)
        return result
