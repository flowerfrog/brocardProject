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
        main_page.admin_must_be_authorized(user)


@allure.epic('Authorized')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_authorization_registered_customer():

    user = User(
        name=os.getenv('CUSTOMER_NAME'),
        email=os.getenv('CUSTOMER_EMAIL'),
        password=os.getenv('CUSTOMER_PASSWORD')
    )

    with allure.step("Open the main page"):
        main_page.open()

    with allure.step("Set cookies for authorized without 2FA"):
        main_page.set_cookie_authorized_without_2fa(cookie_name=os.getenv('COOKIE_NAME'),
                                                    cookie_value=os.getenv('COOKIE_VALUE'))

    with allure.step("Filling the authorization form"):
        main_page.filling_authorization_form(user)

    with allure.step("Checking that user has been authorized"):
        main_page.customer_must_be_authorized(user)


@allure.epic('Authorized')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_authorization_unregistered_user():

    user = User(
        name=os.getenv('UNREGISTERED_USER_NAME'),
        email=os.getenv('UNREGISTERED_USER_EMAIL'),
        password=os.getenv('UNREGISTERED_USER_PASSWORD')
    )

    with allure.step("Open the main page"):
        main_page.open()

    with allure.step("Set cookies for authorized without 2FA"):
        main_page.set_cookie_authorized_without_2fa(cookie_name=os.getenv('COOKIE_NAME'),
                                                    cookie_value=os.getenv('COOKIE_VALUE'))

    with allure.step("Filling the authorization form"):
        main_page.filling_authorization_form(user)

    with allure.step("Checking that user has not been authorized"):
        main_page.unregistered_user_must_not_be_authorized()
