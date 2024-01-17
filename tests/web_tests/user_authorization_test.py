import os
import allure
from brocard_project.data.users import User
from brocard_project.pages.main_page import main_page


@allure.epic('Authorized')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_authorization_registered_admin():

    user = User(
        name=os.getenv('ADMIN_NAME'),
        email=os.getenv('ADMIN_EMAIL'),
        password=os.getenv('ADMIN_PASSWORD')
    )

    with allure.step("Open the main page"):
        main_page.open()

    with allure.step("Filling the authorization form"):
        main_page.filling_authorization_form(user)

    with allure.step("Checking that user has been authorized"):
        main_page.user_must_be_authorized(user)
