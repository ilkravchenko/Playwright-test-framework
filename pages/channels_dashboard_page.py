from playwright.sync_api import Page

from page_factory.button import Button
from pages.base_page import BasePage


class ChannelDashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.new_channel_button = Button(page, locator='button[aria-label="New channel"]', name="New channel")

    def click_create_channel(self):
        self.new_channel_button.click()

    def check_channel_exists(self, channel_name):
        self.entities_panel.entitie_name.should_be_visible()
        self.entities_panel.entitie_name.should_have_text(channel_name)
