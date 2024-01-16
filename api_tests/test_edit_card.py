import allure
import jsonschema
from api_tests.utils import load_schema, load_env
from api_tests.utils import brocard_api_put


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Editing a card title')
def test_edit_card_title():
    card_id = 1314861
    card_title = 'test_change_name_card'
    API_KEY = load_env()
    url = f"/cards/{card_id}"
    schema = load_schema('cards/put_edit_card.json')

    result = brocard_api_put(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "title": card_title
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['title'] == card_title


@allure.tag("api")
@allure.label("owner", "flowerfrog")
@allure.feature('API')
@allure.story('Editing a card owner')
def test_edit_card_owner():
    card_id = 1314861
    user_id = 4
    API_KEY = load_env()
    url = f"/cards/{card_id}"
    schema = load_schema('cards/put_edit_card.json')

    result = brocard_api_put(url,
                             headers={
                                 "Authorization": f'Bearer {API_KEY}',
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"
                             },
                             params={
                                 "user_id": user_id
                             })

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['user']['id'] == user_id
