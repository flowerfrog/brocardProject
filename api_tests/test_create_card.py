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
    schema = load_schema('cards/post_successful_create_limit_card.json')

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


@pytest.mark.skip
def test_create_balance_card_successful():
    card_bin = '436797'
    card_title = 'test_creating_card'
    card_balance = '25.35'
    transaction_limit = '50.00'
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/post_successful_create_balance_card.json')

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
                               "balance": card_balance
                           })

    assert result.status_code == 201
    jsonschema.validate(result.json(), schema)
    assert result.json()['title'] == card_title
    assert result.json()['bin'] == card_bin
    assert result.json()['balance_type'] == "card_balance"
    assert result.json()['available'] == card_balance
    assert result.json()['state']['label'] == "Active"
    assert result.json()['limits'][0]['type'] == "transaction_limit"
    assert result.json()['limits'][0]['amount'] == transaction_limit


def test_create_balance_card_with_balance_less_minimum():
    card_bin = '436797'
    card_title = 'test_creating_card'
    card_balance = '24'
    transaction_limit = '50.00'
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/post_unsuccessful_create_card.json')

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
                               "balance": card_balance
                           })

    assert result.status_code == 422
    jsonschema.validate(result.json(), schema)
    assert result.json()['message'] == "The balance must be greater than or equal 25."
    assert result.json()['errors']['balance'][0] == "The balance must be greater than or equal 25."


def test_create_balance_card_with_balance_more_user_balance():
    card_bin = '436797'
    card_title = 'test_creating_card'
    card_balance = '2000.00'
    transaction_limit = '50.00'
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/post_unsuccessful_create_balance_card.json')

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
                               "balance": card_balance
                           })

    assert result.status_code == 422
    jsonschema.validate(result.json(), schema)
    assert result.json()['message'] == "Not enough user balance."


def test_create_balance_card_with_transaction_limit_more_available_user_limit():
    card_bin = '436797'
    card_title = 'test_creating_card'
    card_balance = '25.00'
    transaction_limit = '10000.00'
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/post_unsuccessful_create_balance_card.json')

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
                               "balance": card_balance
                           })

    assert result.status_code == 422
    jsonschema.validate(result.json(), schema)
    assert result.json()['message'] == "Limit per transaction must not exceed the value in the profile settings"


def test_create_limit_card_with_transaction_limit_less_minimum():
    card_bin = '485953'
    card_title = 'test_creating_card'
    transaction_limit = '49.00'
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/post_unsuccessful_create_card.json')

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
    schema = load_schema('cards/post_unsuccessful_create_card.json')

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


def test_create_limit_card_with_autotopup():
    card_bin = '485953'
    card_title = 'test_creating_card'
    transaction_limit = '50.00'
    total_limit = '50.00'
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/post_unsuccessful_create_card.json')

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
                               "total_limit": total_limit,
                               "topup_auto": "true"
                           })

    assert result.status_code == 422
    jsonschema.validate(result.json(), schema)
    assert result.json()[
               'message'] == "The topup_auto prohibited if card has deferred state. Also prohibited for BIN without card_balance support."
    assert result.json()['errors']['topup_auto'][
               0] == "The topup_auto prohibited if card has deferred state. Also prohibited for BIN without card_balance support."


def test_create_card_without_title():
    card_bin = '485953'
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/post_unsuccessful_create_card.json')

    result = requests.post(url,
                           headers={
                               "Authorization": f'Bearer {API_KEY}',
                               "Content-Type": "application/json",
                               "Accept": "application/json"
                           },
                           params={
                               "bin": card_bin
                           })

    assert result.status_code == 422
    jsonschema.validate(result.json(), schema)
    assert result.json()['message'] == "The title field is required."
    assert result.json()['errors']['title'][0] == "The title field is required."


def test_create_card_without_bin():
    card_title = 'test_creating_card'
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/post_unsuccessful_create_card.json')

    result = requests.post(url,
                           headers={
                               "Authorization": f'Bearer {API_KEY}',
                               "Content-Type": "application/json",
                               "Accept": "application/json"
                           },
                           params={
                               "title": card_title
                           })

    assert result.status_code == 422
    jsonschema.validate(result.json(), schema)
    assert result.json()['message'] == "The bin field is required."
    assert result.json()['errors']['bin'][0] == "The bin field is required."
