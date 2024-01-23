import os
import allure

from brocard_project.data.companies import Company
from brocard_project.data.users import User
from brocard_project.pages.main_page import main_page
from brocard_project.pages.company_dashboard import company_dashboard
from brocard_project.pages.card_page import card_page


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
        count_active_card='33'
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
