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


company_dashboard = CompanyDashboard()
