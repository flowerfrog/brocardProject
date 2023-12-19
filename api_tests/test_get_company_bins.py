import allure
import jsonschema
from api_tests.utils import load_schema, load_env
from api_tests.utils import brocard_api_get


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Get company bins')
def test_get_company_bins():
    API_KEY = load_env()
    url = "/company/bins"
    schema = load_schema('company/get_company_bins.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 36
