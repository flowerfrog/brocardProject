import allure
import jsonschema
from tests.api_tests.utils import load_env
from tests.api_tests.utils import brocard_api_get
from brocard_project.helpers.load_schema import load_schema


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a payment with a given id')
def test_get_payment_of_company_member_with_given_id():
    API_KEY = load_env()
    payment_id = 31393250
    url = f"/payments/{payment_id}"
    schema = load_schema('payments/get_show_payment.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['id'] == 31393250


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a payment with a given id')
def test_get_payment_of_non_company_member_with_given_id():
    API_KEY = load_env()
    payment_id = 31393251
    url = f"/payments/{payment_id}"
    schema = load_schema('payments/get_show_payments_non_company_member.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             })

    assert result.status_code == 403
    jsonschema.validate(result.json(), schema)
    assert result.json()['message'] == "This action is unauthorized."
