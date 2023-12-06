import jsonschema
import requests
from tests.utils import load_schema, load_env


def test_get_balance_card():
    card_bin = '540542'
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/get_balance_cards.json')

    result = requests.get(url,
                          headers={
                              "Authorization": f'Bearer {API_KEY}',
                              "Content-Type": "application/json",
                              "Accept": "application/json"
                          },
                          params={"bins[]": card_bin})

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['bin'] == card_bin
    assert result.json()['data'][0]['currency'] == 'USD'
    assert result.json()['data'][0]['balance_type'] == 'card_balance'


def test_get_limit_card():
    card_bin = '485953'
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/cards"
    schema = load_schema('cards/get_limit_cards.json')

    result = requests.get(url,
                          headers={
                              "Authorization": f'Bearer {API_KEY}',
                              "Content-Type": "application/json",
                              "Accept": "application/json"
                          },
                          params={"bins[]": card_bin})

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['bin'] == card_bin
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
    card_id = 1321211
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
                              "ids[]": card_id
                          })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 1
    assert result.json()['data'][0]['id'] == card_id


def test_get_card_with_last_fours():
    last_fours = '0386'
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
                              "last_fours[]": last_fours
                          })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 1
    assert result.json()['data'][0]['last_four'] == last_fours


def test_get_only_archived_cards():
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
                              "archived": 'only'
                          })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['archived'] is True
    assert result.json()['total'] == 669


def test_get_include_archived_cards():
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
                              "archived": 'include'
                          })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['archived'] is True or result.json()['data'][0]['archived'] is False
    assert result.json()['total'] == 693


def test_get_exclude_archived_cards():
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
                              "archived": 'exclude'
                          })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['archived'] is False
    assert result.json()['total'] == 24


def test_get_include_micropayments_cards():
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
                              "micro": 'include'
                          })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['micro_payments_enabled'] is True or result.json()['data'][0]['micro_payments_enabled'] is False
    assert result.json()['total'] == 24


def test_get_only_micropayments_cards():
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
                              "micro": 'only'
                          })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['micro_payments_enabled'] is True
    assert result.json()['total'] == 1


def test_get_exclude_micropayments_cards():
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
                              "micro": 'exclude'
                          })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['micro_payments_enabled'] is False
    assert result.json()['total'] == 23


def test_get_active_cards():
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
                              "states[]": 2
                          })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['state']['value'] == 2
    assert result.json()['data'][0]['state']['label'] == "Active"
    assert result.json()['total'] == 13


def test_get_blocked_cards():
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
                              "states[]": 3
                          })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['state']['value'] == 3
    assert result.json()['data'][0]['state']['label'] == "Blocked"
    assert result.json()['total'] == 10


def test_get_paused_cards():
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
                              "states[]": 4
                          })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['state']['value'] == 4
    assert result.json()['data'][0]['state']['label'] == "Paused"
    assert result.json()['total'] == 1


def test_list_of_cards_pagination():
    page = 2
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
