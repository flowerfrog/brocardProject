import allure
import jsonschema
from tests.api_tests.utils import load_env
from tests.api_tests.utils import brocard_api_get
from brocard_project.helpers.load_schema import load_schema


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of balance cards')
def test_get_balance_card():
    card_bin = '540542'
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_balance_cards.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={"bins[]": card_bin,
                                     "archived": "include"})

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['bin'] == card_bin
    assert result.json()['data'][0]['currency'] == 'USD'
    assert result.json()['data'][0]['balance_type'] == 'card_balance'


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of limit cards')
def test_get_limit_card():
    card_bin = '485953'
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_limit_cards.json')

    result = brocard_api_get(url,
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


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of cards in a given date range')
def test_get_card_with_specified_date():
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
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
    assert len(result.json()['data']) == result.json()['total']


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a card with a given id')
def test_get_card_with_id():
    card_id = 1321211
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "ids[]": card_id,
                                 "archived": "include"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 1
    assert result.json()['data'][0]['id'] == card_id


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a card with a given last fours')
def test_get_card_with_last_fours():
    last_fours = '0386'
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "last_fours[]": last_fours,
                                 "archived": "include"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 1
    assert result.json()['data'][0]['last_four'] == last_fours


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of archived cards')
def test_get_only_archived_cards():
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
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
    # assert result.json()['total'] == 674


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of all cards: archived cards and non archived cards')
def test_get_include_archived_cards():
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
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
    # assert result.json()['total'] == 698


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of non archived cards')
def test_get_exclude_archived_cards():
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
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
    # assert result.json()['total'] == 24


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of all cards: with micropayments and without micropayments')
def test_get_include_micropayments_cards():
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
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
    assert result.json()['data'][0]['micro_payments_enabled'] is True or result.json()['data'][0][
        'micro_payments_enabled'] is False
    # assert result.json()['total'] == 24


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of cards with micropayments')
def test_get_only_micropayments_cards():
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "micro": 'only',
                                 "archived": "include"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['micro_payments_enabled'] is True
    assert len(result.json()['data']) == result.json()['total']


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of cards without micropayments')
def test_get_exclude_micropayments_cards():
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
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
    # assert result.json()['total'] == 23


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of active cards')
def test_get_active_cards():
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
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
    # assert result.json()['total'] == 13


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of blocked cards')
def test_get_blocked_cards():
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
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
    # assert result.json()['total'] == 10


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of paused cards')
def test_get_paused_cards():
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
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
    # assert result.json()['total'] == 1


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of team cards')
def test_get_list_cards_of_team():
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "teams[]": 1
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['user']['team']['id'] == 1
    # assert result.json()['total'] == 24


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of user cards')
def test_get_list_cards_of_user():
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "users[]": 4,
                                 "archived": "include",
                                 "per_page": 1000
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['user']['id'] == 4
    assert len(result.json()['data']) == result.json()['total']


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of cards with a given tag')
def test_get_list_cards_tag():
    card_tag = 'd79bd0a9-5754-4b85-b8bd-59885dc655a1'
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "tags[]": card_tag
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['tags'][0]['uuid'] == card_tag
    assert len(result.json()['data']) == result.json()['total']


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting the next page of the card list')
def test_list_of_cards_pagination():
    page = 2
    API_KEY = load_env()
    url = "/cards"
    schema = load_schema('cards/get_list_cards.json')

    result = brocard_api_get(url,
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


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a set number of items on a page')
def test_list_of_cards_per_page():
    page = 2
    per_page = 6
    API_KEY = load_env()
    url = "/cards"

    result = brocard_api_get(url,
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
