from selene import browser, be, have


class CompanyDashboard:
    def open(self):
        browser.open("company/dashboard")
        return self

    def get_value_of_count_cards_from_active_cards_widget(self, company):
        browser.element('h3.mt-2').should(have.text(company.count_active_card))
        return self

    def clicking_on_link_cards_in_active_card_widget(self):
        browser.element('div:nth-child(1) > div > div > div.mt-3.fs-14 > a').should(be.visible).click()
        return self

    def get_value_of_count_members_from_members_widget(self, company):
        browser.element('div:nth-child(2) > div > div > div:nth-child(1) > h3').should(have.text(company.count_members))
        return self

    def clicking_on_link_members_in_members_widget(self):
        browser.element('div:nth-child(2) > div > div > div.mt-3.fs-14 > a').should(be.visible).click()
        return self

    def get_value_of_count_card_from_released_cards_today_widget(self, company):
        (browser.element('div:nth-child(3) > div > div > div:nth-child(1) > h3')
         .should(have.text(company.count_released_card_today)))
        return self

    def clicking_on_link_cards_in_released_cards_today_widget(self):
        browser.element('div:nth-child(3) > div > div > div.d-flex > a').should(be.visible).click()
        return self

    def choosing_last_month_in_widget_cashback(self):
        browser.element('[data-v-182d5a6c] > [type="button"]').should(be.visible).click()
        browser.element('.dropdown-menu.show > div:nth-child(1)').should(be.visible).click()
        return self

    def get_values_DR_and_sum_cashback_from_widget_cashback(self, company):
        browser.element('h3[data-v-182d5a6c]').should(have.text(company.cashback))
        browser.element('strong[data-v-182d5a6c]').should(have.text(company.decline_rate_for_last_month))
        return self

    def get_value_sum_payments_for_30_days(self, company):
        value_sum = float(company.sum_payments_for_30_days.split('$')[1])
        browser.element('p.h3[data-v-039d2888]').should(have.text(str(round(value_sum, 0))))
        return self

    def clicking_on_link_more_details_in_sum_payments_for_30_days_widget(self):
        browser.element('a[data-v-039d2888]').should(be.visible).click()
        return self

    def get_values_DR7_and_DR30_from_widget_decline_rate(self, company):
        browser.element('p:nth-child(1) > [data-v-039d2888]> span').should(have.text(company.dr_7))
        browser.element('p:nth-child(2) > [data-v-039d2888]> span').should(have.text(company.dr_30))
        return self

    def get_values_from_widget_teams(self, team):
        (browser.element(f'[href="https://private.mybrocard.com/company/members?team_id={team.id}&state=2"]')
         .should(have.text(team.count_members)))
        (browser.element(f'[href="https://private.mybrocard.com/company/cards?team[0]={team.id}&state=2"]')
         .should(have.text(team.count_active_card)))
        browser.element('tbody > tr:nth-child(1) > td[data-v-56a03558]:nth-child(5)').should(have.text(team.spend))
        (browser.element('tbody > tr:nth-child(1) > td[data-v-56a03558]:nth-child(6)')
         .should(have.text(team.total_balance)))
        browser.element('tbody > tr:nth-child(1) > td[data-v-56a03558]:nth-child(8)').should(have.text(team.dr_7))
        browser.element('tbody > tr:nth-child(1) > td[data-v-56a03558]:nth-child(9)').should(have.text(team.dr_30))
        return self

    def clicking_on_link_in_column_members_in_widget_members(self):
        browser.element('tbody > tr:nth-child(1) > td:nth-child(3) > a').should(be.visible).click()
        return self

    def clicking_on_link_in_column_active_cards_in_widget_members(self):
        browser.element('tbody > tr:nth-child(1) > td:nth-child(4) > a').should(be.visible).click()
        return self


company_dashboard = CompanyDashboard()
