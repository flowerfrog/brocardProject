from selene import browser, be


class UserProfilePage:
    def open(self, user):
        browser.open(f"admin/users/{user.id}/profile/summary")
        return self

    def login_as(self, user):
        browser.element(f'[href="https://private.mybrocard.com/admin/users/'
                        f'user/{user.id}/impersonate"]').should(be.visible).click()
        return self


user_profile = UserProfilePage()
