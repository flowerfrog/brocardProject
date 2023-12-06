import jsonschema
import pytest
import requests
from api_tests.utils import load_schema, load_env


@pytest.mark.skip
def test_create_limit_card_successful():
    card_bin = '485953'
    card_title = 'test_creating_card'
    transaction_limit = '50.00'
    total_limit = '50.00'
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/post_successful_create_card.json')

    result = requests.post(url,
                           headers={
                               "Authorization": f'Bearer {API_KEY}',
                               "Content-Type": "application/json",
                               "Accept": "application/json"
                           },
                           params={
                               "bin": card_bin,
                               "title": card_title,
                               "transaction_limit": transaction_limit,
                               "total_limit": total_limit
                           })

    assert result.status_code == 201
    jsonschema.validate(result.json(), schema)
    assert result.json()['title'] == card_title
    assert result.json()['bin'] == card_bin
    assert result.json()['balance_type'] == "account_balance"
    assert result.json()['state']['label'] == "Active"
    assert result.json()['limits'][0]['type'] == "transaction_limit"
    assert result.json()['limits'][0]['amount'] == transaction_limit
    assert result.json()['limits'][1]['type'] == "total_limit"
    assert result.json()['limits'][1]['amount'] == total_limit


def test_create_limit_card_with_transaction_limit_less_minimum():
    card_bin = '485953'
    card_title = 'test_creating_card'
    transaction_limit = '49.00'
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/post_unsuccessful_create_card_with_transaction_limit_less_minimum.json')

    result = requests.post(url,
                           headers={
                               "Authorization": f'Bearer {API_KEY}',
                               "Content-Type": "application/json",
                               "Accept": "application/json"
                           },
                           params={
                               "bin": card_bin,
                               "title": card_title,
                               "transaction_limit": transaction_limit
                           })

    assert result.status_code == 422
    jsonschema.validate(result.json(), schema)
    assert result.json()['message'] == "The transaction_limit must be greater than or equal 50."
    assert result.json()['errors']['transaction_limit'][0] == "The transaction_limit must be greater than or equal 50."


def test_create_limit_card_with_total_limit_less_minimum():
    card_bin = '485953'
    card_title = 'test_creating_card'
    total_limit = '49.00'
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/post_unsuccessful_create_card_with_total_limit_less_minimum.json')

    result = requests.post(url,
                           headers={
                               "Authorization": f'Bearer {API_KEY}',
                               "Content-Type": "application/json",
                               "Accept": "application/json"
                           },
                           params={
                               "bin": card_bin,
                               "title": card_title,
                               "total_limit": total_limit
                           })

    assert result.status_code == 422
    jsonschema.validate(result.json(), schema)
    assert result.json()['message'] == "The total_limit must be greater than or equal 50."
    assert result.json()['errors']['total_limit'][0] == "The total_limit must be greater than or equal 50."
