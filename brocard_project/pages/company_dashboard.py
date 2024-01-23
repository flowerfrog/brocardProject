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


company_dashboard = CompanyDashboard()
