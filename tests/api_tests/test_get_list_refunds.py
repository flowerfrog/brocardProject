import allure
import jsonschema
from tests.api_tests.utils import load_env
from tests.api_tests.utils import brocard_api_get
from brocard_project.helpers.load_schema import load_schema


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of refunds')
def test_get_list_refunds():
    API_KEY = load_env()
    url = "/refunds"
    schema = load_schema('refunds/get_list_refunds.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['data']) == 20


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of refunds in a given date range')
def test_get_refunds_with_specified_date():
    API_KEY = load_env()
    url = "/refunds"
    schema = load_schema('refunds/get_list_refunds.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "dates[begin]": '2023-10-01 00:00:00',
                                 "dates[end]": '2023-11-01 00:00:00',
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert ('2023-10-01 00:00:00' < result.json()['data'][0]['date'] < '2023-11-01 00:00:00')
    assert len(result.json()['data']) == 2


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of refunds with a given bin')
def test_get_refunds_with_given_bin():
    API_KEY = load_env()
    url = "/refunds"
    schema = load_schema('refunds/get_list_refunds.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "bins[]": 556735
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['card']['bin'] == '556735'
    assert len(result.json()['data']) == 2


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of refunds with a given card')
def test_get_refunds_with_given_card():
    API_KEY = load_env()
    url = "/refunds"
    schema = load_schema('refunds/get_list_refunds.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "cards[]": 1251947
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['card']['id'] == 1251947
    assert len(result.json()['data']) == 2


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a refund with a given id')
def test_get_refund_with_given_id():
    API_KEY = load_env()
    url = "/refunds"
    schema = load_schema('refunds/get_list_refunds.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "ids[]": 87381
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['id'] == 87381
    assert len(result.json()['data']) == 1


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a refund with a given team')
def test_get_refund_with_given_team():
    API_KEY = load_env()
    url = "/refunds"
    schema = load_schema('refunds/get_list_refunds.json')

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
    assert len(result.json()['data']) == 7


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a refund with a given user')
def test_get_refund_with_given_user():
    API_KEY = load_env()
    url = "/refunds"
    schema = load_schema('refunds/get_list_refunds.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "users[]": 2
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['user']['id'] == 2
    assert len(result.json()['data']) == 7

