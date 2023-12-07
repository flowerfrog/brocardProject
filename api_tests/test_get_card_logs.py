import jsonschema
import requests
from api_tests.utils import load_schema, load_env
from api_tests.utils import brocard_api_get


def test_get_card_logs_company_member():
    card_id = 343604
    API_KEY = load_env()
    url = f"/cards/{card_id}/log"
    schema = load_schema('cards/get_card_logs.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['card']['id'] == card_id


def test_get_card_logs_non_company_member():
    card_id = 1324141
    API_KEY = load_env()
    url = f"/cards/{card_id}/log"
    schema = load_schema('cards/get_card_logs_non_company_member.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'] == []


def test_list_of_cards_per_page():
    card_id = 343604
    page = 2
    per_page = 6
    API_KEY = load_env()
    url = f"/cards/{card_id}/log"

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "page": page,
                                 "per_page": per_page
                             })

    assert result.json()["per_page"] == per_page
    assert len(result.json()['data']) == per_page
