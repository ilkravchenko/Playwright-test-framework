from playwright.sync_api import Page

from pages.base_page import BasePage
from page_factory.button import Button
from page_factory.input import Input


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = Input(page, locator="input[name='email']", name='Username input')
        self.password_input = Input(page, locator="input[name='password']", name='Password input')
        self.login_button = Button(page, locator="button[type='submit']", name='Login button')

    def login(self, username: str, password: str):
        self.email_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
