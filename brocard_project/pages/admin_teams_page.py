from selene import browser, be, have, command


class TeamsPage:
    def open(self):
        browser.open("admin/teams")
        return self

    def choosing_team_in_the_filter_and_applying_the_filter(self, team):
        browser.element('div.row > div:nth-child(2) > input').should(be.visible).type(team.name)
        browser.element('.btn.btn-primary').should(be.visible).click()
        return self

    def get_values_DR7_and_DR30_from_teams(self, team):
        browser.element('tbody > tr > td:nth-child(9)').should(have.text(team.dr_7))
        browser.element('tbody > tr > td:nth-child(10)').should(have.text(team.dr_30))
        return self


teams_page = TeamsPage()
