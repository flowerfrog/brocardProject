from dotenv import load_dotenv
from selene import browser, be, have


class MainPage:
    def open(self):
        browser.open("login")
        return self

    def set_cookie_authorized_without_2fa(self, cookie_name, cookie_value):
        browser.driver.add_cookie(dict(name=cookie_name, value=cookie_value))
        return self

    def filling_authorization_form(self, user):
        browser.element('[id="email"]').should(be.visible).type(user.email)
        browser.element('[id="password"]').should(be.visible).type(user.password)
        browser.element('[type="submit"]').should(be.visible).click()
        return self

    def admin_must_be_authorized(self, user):
        browser.element('.email.text-muted').should(have.text(user.email))
        return self

    def customer_must_be_authorized(self, user):
        browser.element('[href="https://private.mybrocard.com/profile"] > div > .sub').should(have.text(user.email))
        return self


main_page = MainPage()
