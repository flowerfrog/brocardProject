import jsonschema
import requests
from tests.utils import load_schema, load_env


def test_get_balance_card():
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/get_balance_cards.json')

    result = requests.get(url,
                          headers={
                              "Authorization": f'Bearer {API_KEY}',
                              "Content-Type": "application/json",
                              "Accept": "application/json"
                          },
                          params={"bins[]": "540542"})

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['bin'] == '540542'
    assert result.json()['data'][0]['currency'] == 'USD'
    assert result.json()['data'][0]['balance_type'] == 'card_balance'


def test_get_limit_card():
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/get_limit_cards.json')

    result = requests.get(url,
                          headers={
                              "Authorization": f'Bearer {API_KEY}',
                              "Content-Type": "application/json",
                              "Accept": "application/json"
                          },
                          params={"bins[]": "485953"})

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['bin'] == '485953'
    assert result.json()['data'][0]['currency'] == 'USD'
    assert result.json()['data'][0]['balance_type'] == 'account_balance'


def test_get_card_with_specified_date():
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = requests.get(url,
                          headers={
                              "Authorization": f'Bearer {API_KEY}',
                              "Content-Type": "application/json",
                              "Accept": "application/json"
                          },
                          params={
                              "dates[begin]": '2023-11-01 00:00:00',
                              "dates[end]": '2023-12-01 00:00:00',
                          })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert ('2023-11-01 00:00:00' < result.json()['data'][0]['date'] < '2023-12-01 00:00:00')
    assert result.json()['total'] == 7


def test_get_card_with_id():
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = requests.get(url,
                          headers={
                              "Authorization": f'Bearer {API_KEY}',
                              "Content-Type": "application/json",
                              "Accept": "application/json"
                          },
                          params={
                              "ids[]": '1321211'
                          })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 1
    assert result.json()['data'][0]['id'] == 1321211


def test_list_of_cards_pagination():
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    page = 2
    schema = load_schema('cards/get_list_cards.json')

    result = requests.get(url,
                          headers={
                              "Authorization": f'Bearer {API_KEY}',
                              "Content-Type": "application/json",
                              "Accept": "application/json"
                          },
                          params={
                              "page": page,
                              "archived": "include"
                          })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['current_page'] == page


def test_list_of_cards_per_page():
    page = 2
    per_page = 6
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"

    result = requests.get(url,
                          headers={
                              "Authorization": f'Bearer {API_KEY}',
                              "Content-Type": "application/json",
                              "Accept": "application/json"
                          },
                          params={
                              "page": page,
                              "per_page": per_page,
                              "archived": "include"
                          })

    assert result.json()["per_page"] == per_page
    assert len(result.json()['data']) == per_page
