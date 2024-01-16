import allure
import jsonschema
from tests.api_tests.utils import load_schema, load_env
from tests.api_tests.utils import brocard_api_get


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of topups')
def test_get_list_topups():
    API_KEY = load_env()
    url = "/top-ups"
    schema = load_schema('topups/get_list_topups.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['data']) == 44


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of topups with given state')
def test_get_list_pending_topups():
    API_KEY = load_env()
    url = "/top-ups"
    schema = load_schema('topups/get_list_topups.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "states[]": 1
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['data']) == 3
    assert result.json()['data'][0]['state']['value'] == 1
    assert result.json()['data'][0]['state']['label'] == "Pending"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of topups with given state')
def test_get_list_committed_topups():
    API_KEY = load_env()
    url = "/top-ups"
    schema = load_schema('topups/get_list_topups.json')

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
    assert len(result.json()['data']) == 9
    assert result.json()['data'][0]['state']['value'] == 2
    assert result.json()['data'][0]['state']['label'] == "Committed"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of topups with given state')
def test_get_list_processing_error_topups():
    API_KEY = load_env()
    url = "/top-ups"
    schema = load_schema('topups/get_list_topups.json')

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
    assert len(result.json()['data']) == 0


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of topups with given state')
def test_get_list_expired_topups():
    API_KEY = load_env()
    url = "/top-ups"
    schema = load_schema('topups/get_list_topups.json')

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
    assert len(result.json()['data']) == 8
    assert result.json()['data'][0]['state']['value'] == 4
    assert result.json()['data'][0]['state']['label'] == "Expired"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of topups with given state')
def test_get_list_reverted_topups():
    API_KEY = load_env()
    url = "/top-ups"
    schema = load_schema('topups/get_list_topups.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "states[]": 5
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['data']) == 24
    assert result.json()['data'][0]['state']['value'] == 5
    assert result.json()['data'][0]['state']['label'] == "Reverted"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of topups in a given date range')
def test_get_list_topups_with_specified_date():
    dates_begin = "2023-05-01 00:00:00"
    dates_end = "2023-12-01 23:59:59"
    API_KEY = load_env()
    url = "/top-ups"
    schema = load_schema('topups/get_list_topups.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "dates[begin]": dates_begin,
                                 "dates[end]": dates_end
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['data']) == 3
    assert (dates_begin < result.json()['data'][0]['date'] < dates_end)


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of topups with given id')
def test_get_list_topups_with_specified_id():
    API_KEY = load_env()
    url = "/top-ups"
    schema = load_schema('topups/get_list_topups.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "ids[]": 82653
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['data']) == 1
    assert result.json()['data'][0]['id'] == 82653


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of topups with given methods')
def test_get_list_topups_with_other_methods():
    API_KEY = load_env()
    url = "/top-ups"
    schema = load_schema('topups/get_list_topups.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "methods[]": "other"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['data']) == 5
    assert result.json()['data'][0]['method'] == "other"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of topups with given methods')
def test_get_list_topups_with_marketcall_methods():
    API_KEY = load_env()
    url = "/top-ups"
    schema = load_schema('topups/get_list_topups.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "methods[]": "marketcall"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['data']) == 5
    assert result.json()['data'][0]['method'] == "marketcall"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of topups with given methods')
def test_get_list_topups_with_capitalist_methods():
    API_KEY = load_env()
    url = "/top-ups"
    schema = load_schema('topups/get_list_topups.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "methods[]": "capitalist"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['data']) == 8
    assert result.json()['data'][0]['method'] == "capitalist"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of topups with given methods')
def test_get_list_topups_with_usdt_trc_methods():
    API_KEY = load_env()
    url = "/top-ups"
    schema = load_schema('topups/get_list_topups.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "methods[]": "usdt_trc"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['data']) == 3
    assert result.json()['data'][0]['method'] == "usdt_trc"
