import os
import allure

from brocard_project.data.companies import Company
from brocard_project.data.users import User
from brocard_project.pages.main_page import main_page
from brocard_project.pages.company_dashboard import company_dashboard
from brocard_project.pages.card_page import card_page
from brocard_project.pages.payments_page import payment_page


@allure.epic('Statistics')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the display of statistics in the widget of the number of active company cards ")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_stats_in_widget_active_card_of_company():

    user = User(
        name=os.getenv('CUSTOMER_NAME'),
        email=os.getenv('CUSTOMER_EMAIL'),
        password=os.getenv('CUSTOMER_PASSWORD')
    )

    company = Company(
        name='',
        count_active_card='37',
        count_members='',
        count_released_card_today='',
        cashback='',
        decline_rate_for_last_month=''
    )

    with allure.step("Open the company dashboard"):
        main_page.open()
        main_page.set_cookie_authorized_without_2fa(cookie_name=os.getenv('COOKIE_NAME'),
                                                    cookie_value=os.getenv('COOKIE_VALUE'))
        main_page.filling_authorization_form(user)

    with allure.step("Get the value of the number of active cards on the company's dashboard"):
        company_dashboard.get_value_of_count_cards_from_active_cards_widget(company)
        company_dashboard.clicking_on_link_cards_in_active_card_widget()

    with allure.step("Compare the obtained value with the value of the number of active company "
                     "cards in the list of cards"):
        card_page.choosing_to_display_number_of_items_per_page()
        card_page.choosing_to_all_cards_in_list()
        card_page.get_value_of_count_active_company_cards(company)


@allure.epic('Statistics')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the display of statistics in the widget of the number of company members")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_stats_in_widget_members():

    user = User(
        name=os.getenv('CUSTOMER_NAME'),
        email=os.getenv('CUSTOMER_EMAIL'),
        password=os.getenv('CUSTOMER_PASSWORD')
    )

    company = Company(
        name='',
        count_active_card='',
        count_members='117',
        count_released_card_today='',
        cashback='',
        decline_rate_for_last_month=''
    )

    with allure.step("Open the company dashboard"):
        main_page.open()
        main_page.set_cookie_authorized_without_2fa(cookie_name=os.getenv('COOKIE_NAME'),
                                                    cookie_value=os.getenv('COOKIE_VALUE'))
        main_page.filling_authorization_form(user)

    with allure.step("Get the value of the number of members on the company's dashboard"):
        company_dashboard.get_value_of_count_members_from_members_widget(company)
        company_dashboard.clicking_on_link_members_in_members_widget()

    with allure.step("Compare the obtained value with the value of the number "
                     "of company members in the list of members"):
        card_page.get_value_of_count_company_members(company)


@allure.epic('Statistics')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the display of statistics in the widget of the number of released cards today")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_stats_in_widget_released_cards_today():

    user = User(
        name=os.getenv('CUSTOMER_NAME'),
        email=os.getenv('CUSTOMER_EMAIL'),
        password=os.getenv('CUSTOMER_PASSWORD')
    )

    company = Company(
        name='',
        count_active_card='',
        count_members='',
        count_released_card_today='0',
        cashback='',
        decline_rate_for_last_month=''
    )

    with allure.step("Open the company dashboard"):
        main_page.open()
        main_page.set_cookie_authorized_without_2fa(cookie_name=os.getenv('COOKIE_NAME'),
                                                    cookie_value=os.getenv('COOKIE_VALUE'))
        main_page.filling_authorization_form(user)

    with allure.step("Get the value of the number of released cards today on the company's dashboard"):
        company_dashboard.get_value_of_count_card_from_released_cards_today_widget(company)
        company_dashboard.clicking_on_link_cards_in_released_cards_today_widget()

    with allure.step("Compare the obtained value with the value of the number of released cards today"
                     " in the list of cards"):
        card_page.get_value_of_count_released_cards_today(company)


@allure.epic('Statistics')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the display of statistics in the widget cashback")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_stats_in_widget_cashback():

    user = User(
        name=os.getenv('CUSTOMER_NAME'),
        email=os.getenv('CUSTOMER_EMAIL'),
        password=os.getenv('CUSTOMER_PASSWORD')
    )

    company = Company(
        name='',
        count_active_card='',
        count_members='',
        count_released_card_today='',
        cashback='$0.13',
        decline_rate_for_last_month='11.11%'
    )

    with allure.step("Open the company dashboard"):
        main_page.open()
        main_page.set_cookie_authorized_without_2fa(cookie_name=os.getenv('COOKIE_NAME'),
                                                    cookie_value=os.getenv('COOKIE_VALUE'))
        main_page.filling_authorization_form(user)

    with allure.step("Get the values DR and sum cashback of the widget"):
        company_dashboard.choosing_last_month_in_widget_cashback()
        company_dashboard.get_values_DR_and_sum_cashback_from_widget_cashback(company)

    with allure.step("Open the payments page by month with applying filter: date = last month"):
        payment_page.open_page_payments_by_month()
        payment_page.applying_filter_date_last_month()

    with allure.step("Get the values DR and sum cashback of the payments page"):
        payment_page.get_value_DR(company)
        payment_page.get_sum_cashback(company)
