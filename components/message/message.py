from playwright.sync_api import Page

from page_factory.title import Title


class Message:
    def __init__(self, page: Page):
        self.page = page

        self.message_text = Title(page, locator="//span[@ng-bind-html='message.content']", name="Message text")

    def check_message_text(self, text):
        self.message_text.should_be_visible()
        self.message_text.should_have_text(text)
