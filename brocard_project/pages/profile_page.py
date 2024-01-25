from selene import browser, be


class ProfilePage:
    def open(self):
        browser.open("profile")
        return self

    def logout(self):
        browser.element('[for=submit-logout-form]').should(be.visible).click()
        return self

    def stop_impersonate(self):
        browser.element('[href="https://private.mybrocard.com/admin/users'
                        '/user/impersonate/stop"]').should(be.visible).click()
        return self


profile_page = ProfilePage()
