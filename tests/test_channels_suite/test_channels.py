import allure
from pages.channel_creation_page import ChannelCreationPage
from pages.channels_dashboard_page import ChannelDashboardPage
from pages.dashboard_page import DashboardPage


@allure.feature('Channels')
@allure.story('Channels Suite')
class TestLogin:

    @allure.title('Test create Channel')
    def test_create_channel(
        self,
        dashboard_page: DashboardPage,
        channel_dashboard_page: ChannelDashboardPage,
        channel_creation_page: ChannelCreationPage
    ):
        dashboard_page.visit()
        dashboard_page.navbar.hover_channels_list_item()
        dashboard_page.navbar.visit_channels()

        channel_dashboard_page.click_create_channel()

        channel_creation_page.has_page_title()
        channel_name = channel_creation_page.create_channel()
        channel_dashboard_page.check_channel_exists(channel_name)
