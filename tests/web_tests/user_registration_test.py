import os
import allure
import pytest

from brocard_project.data.users import NewUser
from brocard_project.pages.registration_page import registration_page


@allure.epic('Registration')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the registration of the user")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
@pytest.mark.skip(reason='An unused email address is required to register')
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


@allure.epic('Registration')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the registration of the user")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_registration_user_with_invalid_email():

    user = NewUser(
        name=os.getenv('REGISTRATION_USER_NAME'),
        email=os.getenv('INVALID_USER_EMAIL'),
        password=os.getenv('REGISTRATION_USER_PASSWORD'),
        confirm_password=os.getenv('CONFORMATION_REGISTRATION_USER_PASSWORD')
    )

    with allure.step("Open the register page"):
        registration_page.open()

    with allure.step("Filling the registration form"):
        registration_page.filling_registration_form(user)

    with allure.step("Checking that user has not been registered"):
        registration_page.user_must_not_be_registered_with_invalid_email()


@allure.epic('Registration')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the registration of the user")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_registration_user_with_invalid_password():

    user = NewUser(
        name=os.getenv('REGISTRATION_USER_NAME'),
        email=os.getenv('INVALID_USER_EMAIL'),
        password=os.getenv('INVALID_USER_PASSWORD'),
        confirm_password=os.getenv('INVALID_USER_PASSWORD')
    )

    with allure.step("Open the register page"):
        registration_page.open()

    with allure.step("Filling the registration form"):
        registration_page.filling_registration_form(user)

    with allure.step("Checking that user has not been registered"):
        registration_page.user_must_not_be_registered_with_invalid_password()


@allure.epic('Registration')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the registration of the user")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_registration_user_with_invalid_confirm_password():

    user = NewUser(
        name=os.getenv('REGISTRATION_USER_NAME'),
        email=os.getenv('INVALID_USER_EMAIL'),
        password=os.getenv('REGISTRATION_USER_PASSWORD'),
        confirm_password=os.getenv('INVALID_USER_CONFIRM_PASSWORD')
    )

    with allure.step("Open the register page"):
        registration_page.open()

    with allure.step("Filling the registration form"):
        registration_page.filling_registration_form(user)

    with allure.step("Checking that user has not been registered"):
        registration_page.user_must_not_be_registered_with_invalid_confirm_password()
