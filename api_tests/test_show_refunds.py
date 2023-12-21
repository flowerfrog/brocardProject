import allure
import jsonschema
from api_tests.utils import load_schema, load_env
from api_tests.utils import brocard_api_get


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a refund with a given id')
def test_get_refund_of_company_member_with_given_id():
    API_KEY = load_env()
    refund_id = 80078
    url = f"/refunds/{refund_id}"
    schema = load_schema('refunds/get_show_refund.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['id'] == 80078


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a refund with a given id')
def test_get_refund_of_non_company_member_with_given_id():
    API_KEY = load_env()
    refund_id = 92976
    url = f"/refunds/{refund_id}"
    schema = load_schema('refunds/get_show_refund_non_company_member.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             })

    assert result.status_code == 403
    jsonschema.validate(result.json(), schema)
    assert result.json()['message'] == "This action is unauthorized."
