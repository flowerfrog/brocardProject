import allure
import jsonschema
from tests.api_tests.utils import load_env
from tests.api_tests.utils import brocard_api_get
from brocard_project.helpers.load_schema import load_schema


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of tags')
def test_get_list_tags_of_company_member():
    API_KEY = load_env()
    url = "/tags"
    schema = load_schema('tags/get_list_tags.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "users[]": 4
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['data']) == result.json()['total']
    assert result.json()['total'] == 5
    assert result.json()['data'][0]['user']['id'] == 4


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of tags')
def test_get_list_tags_of_non_company_member():
    API_KEY = load_env()
    url = "/tags"
    schema = load_schema('tags/get_list_tags.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "users[]": 5
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 0
