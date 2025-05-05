from playwright.sync_api import Page

from models.channel import CreateChannel

from page_factory.button import Button
from page_factory.input import Input
from page_factory.radio_button import RadioButton
from page_factory.unordered_list import UnorderedList
from pages.base_page import BasePage


class ChannelCreationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_button = Button(page, locator="button[aria-label='Save']", name="Create")

        #  Primary fields
        self.channel_name_input = Input(page, locator="input[name='given_name']", name="Channel Name")
        self.client_revshare_input = Input(page, locator="input[name='rate']", name="Client's revshare")

        #  Non-primary fields
        self.channel_description_input = Input(page, locator="input[name='rate']", name="Channel")
        self.channel_type_radio_button = RadioButton(
            page,
            locator="radio-button-group[aria-label='Channel type'] div[class='btn-group-wrapper']",
            name="Channel Type")
        self.seller_type_unordered_list = UnorderedList(
            page,
            locator="div[name='ui-select-vefhncz'] span[class='ui-select-match-text pull-left'] span",
            name="Seller type")

        self.success_message = "Saved Successfully"

    def has_page_title(self):
        self.entities_panel.create_channel_title.should_be_visible()
        self.entities_panel.create_channel_title.should_have_text(self.entities_panel.create_channel_title.name)

    def check_primary_values(self, channel_model):
        self.channel_name_input.should_have_value(channel_model.name)
        self.client_revshare_input.should_have_value(channel_model.client_revshare)

    def create_channel(self):
        channel_input = CreateChannel()
        self.channel_name_input.fill(channel_input.name)
        self.client_revshare_input.fill(channel_input.client_revshare)

        self.create_button.click()
        self.message.check_message_text("Saved successfully")
        self.check_primary_values(channel_input)
        return channel_input.name
