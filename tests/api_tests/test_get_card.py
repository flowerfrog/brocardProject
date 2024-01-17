import allure
import jsonschema
from tests.api_tests.utils import load_env
from tests.api_tests.utils import brocard_api_get
from brocard_project.helpers.load_schema import load_schema


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting card data')
def test_show_company_member_card():
    card_id = 1314861
    API_KEY = load_env()
    url = f"/cards/{card_id}"
    schema = load_schema('cards/get_card_company_member.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['id'] == card_id


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting card data')
def test_show_non_company_member_card():
    card_id = 666
    API_KEY = load_env()
    url = f"/cards/{card_id}"
    schema = load_schema('cards/get_card_non_company_member.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             })

    assert result.status_code == 403
    jsonschema.validate(result.json(), schema)
    assert result.json()['message'] == 'You do not have permission to view card.'
