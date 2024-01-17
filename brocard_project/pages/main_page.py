from selene import browser, be, have


class MainPage:
    def open(self):
        browser.open("login")
        return self

    def filling_authorization_form(self, user):
        browser.element('[id="email"]').should(be.visible).type(user.email)
        browser.element('[id="password"]').should(be.visible).type(user.password)
        browser.element('[type="submit"]').should(be.visible).click()
        return self

    def user_must_be_authorized(self, user):
        browser.element('.email.text-muted').should(have.text(user.email))
        return self


main_page = MainPage()
