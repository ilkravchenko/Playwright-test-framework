import allure

from pages.dashboard_page import DashboardPage


@allure.feature('Logout')
@allure.story('Logout Suite')
class TestLogin:

    @allure.title('Logout Test')
    def test_logout(self, dashboard_page: DashboardPage):
        dashboard_page.visit()
        dashboard_page.navbar.logout()
