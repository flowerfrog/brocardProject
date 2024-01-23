from selene import browser, be, have


class PaymentPage:
    def open(self):
        browser.open("company/payments")
        return self

    def open_page_payments_by_month(self):
        browser.open("company/payments/group-by/month")
        return self

    def applying_filter_date_last_month(self):
        browser.element('div.form-control[data-v-1ebd09d2]').should(be.visible).click()
        browser.element('div.calendars > div > ul > li:nth-child(6)').should(be.visible).click()
        browser.element('div.card-body > div > .btn.btn-primary').should(be.visible).click()
        return self

    def get_value_DR(self, company):
        browser.element('tbody > tr > td:nth-child(15)').should(have.text(company.decline_rate_for_last_month))
        return self

    def get_sum_cashback(self, company):
        value_cashback = float(company.cashback.split('$')[1])
        value_dr = float(company.decline_rate_for_last_month.split('%')[0])
        if value_dr < 5:
            browser.element('tbody > tr > td:nth-child(13)').should(have.text(str(value_cashback)))
        if 5 <= value_dr < 10:
            browser.element('tbody > tr > td:nth-child(13)').should(have.text(str(round((value_cashback * 2), 1))))
        if 10 <= value_dr < 15:
            browser.element('tbody > tr > td:nth-child(13)').should(have.text(str(round((value_cashback * 4), 1))))
        return self


payment_page = PaymentPage()
