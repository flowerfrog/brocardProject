from selene import browser, have, command


class MembersPage:
    def open(self):
        browser.open("company/members")
        return self

    def get_values_total_balance_and_spend(self, team):
        browser.element('div:nth-child(1) > strong[data-v-0a9f5661]').should(have.text(team.total_balance))
        browser.element('div:nth-child(2) > strong[data-v-0a9f5661]').should(have.text(team.spend))
        return self

    def get_count_members_of_team(self, team):
        results = (browser.all('tbody[data-v-0a93b396] > tr'))
        results.should(have.size(int(team.count_members)))
        browser.element('.row.mt-3.fs-14').perform(command.js.scroll_into_view)
        return self


members_page = MembersPage()
