from selene import browser, be, have, command


class CompaniesPage:
    def open(self):
        browser.open("admin/companies")
        return self

    def choosing_company_in_the_filter_and_applying_the_filter(self, company):
        browser.element('div:nth-child(5) > div > div > div.multiselect__tags').should(be.visible).click()
        browser.element('[placeholder="ID, название"]').should(be.visible).type(company.name)
        browser.element('div:nth-child(5) > div > div > .multiselect__content-wrapper > '
                        'ul > li:nth-child(1) > span > span').should(have.text(company.name))
        browser.element('[placeholder="ID, название"]').press_enter()
        browser.element('.btn.btn-primary').should(be.visible).click()
        browser.element('footer.footer').perform(command.js.scroll_into_view)
        return self

    def get_values_DR7_and_DR30_from_companies(self, company):
        browser.element('tbody > tr > td:nth-child(12)').should(have.text(company.dr_7))
        browser.element('tbody > tr > td:nth-child(13)').should(have.text(company.dr_30))
        return self


companies_page = CompaniesPage()
