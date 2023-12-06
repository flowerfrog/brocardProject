import jsonschema
import requests
from api_tests.utils import load_schema, load_env


def test_get_list_balance():
    API_KEY = load_env()
    url = "https://private.mybrocard.com/api/v2/balance"
    schema = load_schema('balance/get_list_balance.json')
    result = requests.get(url, headers={
        "Authorization": f'Bearer {API_KEY}',
        "Content-Type": "application/json",
        "Accept": "application/json"
    })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['data'][0]) == 4
    assert result.json()['data'][0]['total'] == '1501.29'
    assert result.json()['data'][0]['reserved'] == '367.00'
    assert result.json()['data'][0]['available'] == '1134.29'
    assert result.json()['data'][0]['currency'] == 'USD'