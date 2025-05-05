import allure
from playwright.sync_api import Page, Response, expect

from components.entities_left_panel.entities_panel import EntitiesPanel
from components.navigation.navbar import Navbar
from components.message.message import Message
from config import get_ui_config
from page_factory.image import Image


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.message = Message(page)
        self.navbar = Navbar(page)
        self.entities_panel = EntitiesPanel(page)

        self.logo_image = Image(page, locator="img.logo-image", name="Logo image")

    def visit(self) -> Response | None:
        with allure.step(f'Opening the url "{get_ui_config.base_url}"'):
            url = get_ui_config.base_url
            return self.page.goto(url, wait_until='networkidle')

    def reload(self) -> Response | None:
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            return self.page.reload(wait_until='domcontentloaded')

    def page_has_url(self, url: str):
        expect(self.page).to_have_url(url)

    def logo_visible(self):
        self.logo_image.should_be_visible()
