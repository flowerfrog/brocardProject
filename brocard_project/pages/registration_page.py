from selene import browser, be, have


class RegistrationPage:
    def open(self):
        browser.open("register")
        return self

    def filling_registration_form(self, user):
        browser.element('[id="name"]').should(be.visible).type(user.name)
        browser.element('[id="email"]').should(be.visible).type(user.email)
        browser.element('[id="password"]').should(be.visible).type(user.password)
        browser.element('[id="password-confirm"]').should(be.visible).type(user.confirm_password)
        browser.element('[type="submit"]').should(be.visible).click()
        return self

    def user_must_be_registered(self):
        browser.element('.noble-ui-logo').should(have.text('Подключите двухфакторную авторизацию '
                                                           'для безопасности ваших финансов'))
        return self


registration_page = RegistrationPage()
