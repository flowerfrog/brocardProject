import os
import allure
from brocard_project.data.users import NewUser
from brocard_project.pages.registration_page import registration_page


@allure.epic('Registration')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_registration_user():

    user = NewUser(
        name=os.getenv('REGISTRATION_USER_NAME'),
        email=os.getenv('REGISTRATION_USER_EMAIL'),
        password=os.getenv('REGISTRATION_USER_PASSWORD'),
        confirm_password=os.getenv('CONFORMATION_REGISTRATION_USER_PASSWORD')
    )

    with allure.step("Open the register page"):
        registration_page.open()

    with allure.step("Filling the registration form"):
        registration_page.filling_registration_form(user)

    with allure.step("Checking that user has been registered"):
        registration_page.user_must_be_registered()
