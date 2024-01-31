import os
import allure

from brocard_project.data.companies import Company
from brocard_project.data.users import User
from brocard_project.data.teams import Team
from brocard_project.pages.main_page import main_page
from brocard_project.pages.company_dashboard import company_dashboard
from brocard_project.pages.card_page import card_page
from brocard_project.pages.payments_page import payment_page
from brocard_project.pages.profile_page import profile_page
from brocard_project.pages.admin_companies_page import companies_page
from brocard_project.pages.admin_user_profile import user_profile
from brocard_project.pages.members_page import members_page
from brocard_project.pages.admin_teams_page import teams_page


@allure.epic('Statistics')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the display of statistics in the widget of the number of active company cards ")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_stats_in_widget_active_card_of_company():
    user = User(
        id=0,
        name=os.getenv('CUSTOMER_NAME'),
        email=os.getenv('CUSTOMER_EMAIL'),
        password=os.getenv('CUSTOMER_PASSWORD')
    )

    company = Company(
        name='',
        count_active_card='38',
        count_members='',
        count_released_card_today='',
        cashback='',
        decline_rate_for_last_month='',
        sum_payments_for_30_days='',
        dr_7='',
        dr_30=''
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
        id=0,
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
        decline_rate_for_last_month='',
        sum_payments_for_30_days='',
        dr_7='',
        dr_30=''
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
        id=0,
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
        decline_rate_for_last_month='',
        sum_payments_for_30_days='',
        dr_7='',
        dr_30=''
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
        id=0,
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
        decline_rate_for_last_month='11.11%',
        sum_payments_for_30_days='',
        dr_7='',
        dr_30=''
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


@allure.epic('Statistics')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the display of statistics in the widget company payments for 30 days")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_stats_in_widget_company_payments_for_30_days():
    user = User(
        id=0,
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
        decline_rate_for_last_month='11.11%',
        sum_payments_for_30_days='$2.05',
        dr_7='',
        dr_30=''
    )

    with allure.step("Open the company dashboard"):
        main_page.open()
        main_page.set_cookie_authorized_without_2fa(cookie_name=os.getenv('COOKIE_NAME'),
                                                    cookie_value=os.getenv('COOKIE_VALUE'))
        main_page.filling_authorization_form(user)

    with allure.step("Get the value of the sum of company payments for 30 days on the company's dashboard"):
        company_dashboard.get_value_sum_payments_for_30_days(company)
        company_dashboard.clicking_on_link_more_details_in_sum_payments_for_30_days_widget()

    with allure.step("Compare the obtained value with the value of the sum of company payments for 30 days"
                     " in the list of payments"):
        payment_page.get_sum_payments(company)


@allure.epic('Statistics')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the display of statistics in the widget DECLINE RATE COMPANY")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_stats_in_widget_decline_rate():
    user = User(
        id=34071,
        name=os.getenv('CUSTOMER_NAME'),
        email=os.getenv('CUSTOMER_EMAIL'),
        password=os.getenv('CUSTOMER_PASSWORD')
    )

    admin = User(
        id=0,
        name=os.getenv('ADMIN_NAME'),
        email=os.getenv('ADMIN_EMAIL'),
        password=os.getenv('ADMIN_PASSWORD')
    )

    company = Company(
        name="tenebris's company",
        count_active_card='',
        count_members='',
        count_released_card_today='',
        cashback='',
        decline_rate_for_last_month='',
        sum_payments_for_30_days='',
        dr_7='49.25',
        dr_30='39.52'
    )

    with allure.step("Open the company dashboard"):
        main_page.open()
        main_page.filling_authorization_form(admin)
        user_profile.open(user)
        user_profile.login_as(user)

    with allure.step("Get the values DR7 and DR30 of the widget"):
        company_dashboard.get_values_DR7_and_DR30_from_widget_decline_rate(company)

    with allure.step("Open the companies page in the admin cabinet"):
        profile_page.open()
        profile_page.stop_impersonate()
        companies_page.open()

    with allure.step("Checking that the DR values on the company dashboard converge "
                     "with the DR values of the selected company in the companies section"):
        companies_page.choosing_company_in_the_filter_and_applying_the_filter(company)
        companies_page.get_values_DR7_and_DR30_from_companies(company)


@allure.epic('Statistics')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the display of statistics in the widget TEAMS")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_stats_in_widget_teams():
    user = User(
        id=2,
        name=os.getenv('CUSTOMER_NAME'),
        email=os.getenv('CUSTOMER_EMAIL'),
        password=os.getenv('CUSTOMER_PASSWORD')
    )

    admin = User(
        id=0,
        name=os.getenv('ADMIN_NAME'),
        email=os.getenv('ADMIN_EMAIL'),
        password=os.getenv('ADMIN_PASSWORD')
    )

    team = Team(
        id=1,
        name='Малинки',
        count_members='21',
        count_active_card='38',
        spend='$237.06',
        total_balance='$1,449.79',
        dr_7='-',
        dr_30='-'
    )

    with allure.step("Open the company dashboard"):
        main_page.open()
        main_page.filling_authorization_form(admin)
        user_profile.open(user)
        user_profile.login_as(user)

    with allure.step("Get the values of the widget TEAMS"):
        company_dashboard.get_values_from_widget_teams(team)

    with allure.step("Open the members page in the user cabinet"):
        company_dashboard.clicking_on_link_in_column_members_in_widget_members()

    with allure.step("Checking that the values on the company dashboard converge "
                     "with the values of the selected team in the members section"):
        # members_page.get_values_total_balance_and_spend(team)
        members_page.get_count_members_of_team(team)

    with allure.step("Open the teams page in the admin cabinet"):
        profile_page.open()
        profile_page.stop_impersonate()
        teams_page.open()

    with allure.step("Checking that the values on the company dashboard converge "
                     "with the values of the selected team in the teams section"):
        teams_page.choosing_team_in_the_filter_and_applying_the_filter(team)
        teams_page.get_values_DR7_and_DR30_from_teams(team)
