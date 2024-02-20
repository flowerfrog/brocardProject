import allure
import jsonschema
from tests.api_tests.utils import load_env
from tests.api_tests.utils import brocard_api_get
from brocard_project.helpers.load_schema import load_schema


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments')
def test_get_list_payments():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 262


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of settled payments')
def test_get_list_settled_payments():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_settled_payments.json')

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
    assert result.json()['data'][0]['state']['value'] == 1
    assert result.json()['data'][0]['state']['label'] == "Settled"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of pending payments')
def test_get_list_pending_payments():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_pending_payments.json')

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
    assert result.json()['data'][0]['state']['label'] == "Pending"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of void payments')
def test_get_list_void_payments():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_void_payments.json')

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
    assert result.json()['data'][0]['state']['label'] == "Void"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of declined payments')
def test_get_list_declined_payments():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_declined_payments.json')

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
    assert result.json()['data'][0]['state']['label'] == "Declined"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments in a given date range')
def test_get_list_payments_with_specified_date():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "dates[begin]": "2023-12-01 00:00:00",
                                 "dates[end]": "2023-12-10 23:59:59"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 5
    assert ('2023-12-01 00:00:00' < result.json()['data'][0]['date'] < '2023-12-10 23:59:59')


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with a given bins')
def test_get_list_payments_with_given_bin():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "bins[]": 555671
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 4
    assert result.json()['data'][0]['card']['bin'] == '555671'


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with a given countries')
def test_get_list_payments_with_given_country():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "countries[]": 111
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 4
    assert result.json()['data'][0]['merchant']['country']['id'] == 111
    assert result.json()['data'][0]['merchant']['country']['code'] == "IE"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with a given id')
def test_get_list_payments_with_given_id():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "ids[]": 31393250
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 1
    assert result.json()['data'][0]['id'] == 31393250


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with a given merchant')
def test_get_list_payments_with_given_merchant():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "merchants[]": 23
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 2
    assert result.json()['data'][0]['merchant']['id'] == 23
    assert result.json()['data'][0]['merchant']['name'] == "PropellerAds"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of team payments')
def test_get_list_team_payments():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "teams[]": 5151
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 15
    assert result.json()['data'][0]['user']['team']['id'] == 5151
    assert result.json()['data'][0]['user']['team']['name'] == "ежевика"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of user payments')
def test_get_list_user_payments():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

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
    assert result.json()['total'] == 18
    assert result.json()['data'][0]['user']['id'] == 4
    assert result.json()['data'][0]['user']['name'] == "mb"


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of all payments: with micropayments and without micropayments')
def test_get_list_payments_include_micropayments():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "micro": "include"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert (result.json()['data'][0]['is_micro'] is True) or (result.json()['data'][0]['is_micro'] is False)


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with micropayments')
def test_get_list_payments_only_micropayments():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "micro": "only"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['is_micro'] is True


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments without micropayments')
def test_get_list_payments_exclude_micropayments():
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "micro": "exclude"
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['is_micro'] is False


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with decline reason')
def test_get_list_with_decline_reason_balance_less_than_amount():
    decline_reason = 'balance-less-than-amount'
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "declines[]": decline_reason
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 15
    assert result.json()['data'][0]['decline'] == decline_reason


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with decline reason')
def test_get_list_with_decline_reason_limit_transaction_less_than_amount():
    decline_reason = 'limit-transaction-less-than-amount'
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "declines[]": decline_reason
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 1
    assert result.json()['data'][0]['decline'] == decline_reason


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with decline reason')
def test_get_list_with_decline_reason_merchant_not_allowed():
    decline_reason = 'merchant-not-allowed'
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "declines[]": decline_reason
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 16
    assert result.json()['data'][0]['decline'] == decline_reason


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with decline reason')
def test_get_list_with_decline_reason_unknown_mcc():
    decline_reason = 'unknown-mcc'
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "declines[]": decline_reason
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['data'][0]['decline'] == decline_reason


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with decline reason')
def test_get_list_with_decline_reason_asa_disabled():
    decline_reason = 'asa-disabled'
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "declines[]": decline_reason
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 3
    assert result.json()['data'][0]['decline'] == decline_reason


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with decline reason')
def test_get_list_with_decline_reason_asa_disabled():
    decline_reason = 'asa-disabled'
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "declines[]": decline_reason
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 3
    assert result.json()['data'][0]['decline'] == decline_reason


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with decline reason')
def test_get_list_with_decline_reason_card_paused():
    decline_reason = 'card-paused'
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "declines[]": decline_reason
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 6
    assert result.json()['data'][0]['decline'] == decline_reason


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with decline reason')
def test_get_list_with_decline_reason_card_blocked():
    decline_reason = 'card-blocked'
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "declines[]": decline_reason
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 25
    assert result.json()['data'][0]['decline'] == decline_reason


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with decline reason')
def test_get_list_with_decline_reason_declined_by_merchant():
    decline_reason = 'declined-by-merchant'
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "declines[]": decline_reason
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 45
    assert result.json()['data'][0]['decline'] == decline_reason


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with decline reason')
def test_get_list_with_decline_reason_currency_not_allowed():
    decline_reason = 'currency-not-allowed'
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "declines[]": decline_reason
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 1
    assert result.json()['data'][0]['decline'] == decline_reason


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with decline reason')
def test_get_list_with_decline_reason_declined_by_bank():
    decline_reason = 'declined-by-bank'
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "declines[]": decline_reason
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 4
    assert result.json()['data'][0]['decline'] == decline_reason


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Getting a list of payments with decline reason')
def test_get_list_with_decline_reason_card_balance_less_than_amount():
    decline_reason = 'card-balance-less-than-amount'
    API_KEY = load_env()
    url = "/payments-beta"
    schema = load_schema('payments/get_list_payments.json')

    result = brocard_api_get(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "declines[]": decline_reason
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total'] == 8
    assert result.json()['data'][0]['decline'] == decline_reason
