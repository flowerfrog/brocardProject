from selene import browser, have, be, command


class CardPage:
    def open(self):
        browser.open("company/cards")
        return self

    def choosing_to_display_number_of_items_per_page(self):
        browser.element('div:nth-child(3) > button.dropdown-toggle').should(be.visible).click()
        browser.element('div> div.dropdown-menu.show > button:nth-child(4)').should(be.visible).click()
        return self

    def choosing_to_all_cards_in_list(self):
        browser.element('th.checkbox-th > div > label > input').click()
        return self

    def get_value_of_count_active_company_cards(self, company):
        browser.element('span.font-medium:nth-child(3)').should(have.text(company.count_active_card))
        return self

    def get_value_of_count_company_members(self, company):
        browser.element('.row.mt-3.fs-14').perform(command.js.scroll_into_view)
        browser.element('span.font-medium:nth-child(3)').should(have.text(company.count_members))
        return self


card_page = CardPage()
