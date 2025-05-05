from abc import ABC, abstractmethod

import allure
from playwright.sync_api import Locator, Page, expect


class Component(ABC):
    def __init__(self, page: Page, locator: str, name: str) -> None:
        self.page = page
        self.locator = locator
        self.name = name

    @property
    @abstractmethod
    def type_of(self) -> str:
        return "component"

    def get_locator(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.locator(locator)

    def click(self, **kwargs) -> None:
        with allure.step(f"Clicking {self.type_of} with name '{self.name}'"):
            locator = self.get_locator(**kwargs)
            locator.click()

    def hover(self, **kwargs):
        with allure.step(f'Hovering over {self.type_of} with name "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.hover()

    def should_be_visible(self, **kwargs) -> None:
        with allure.step(f"Checking that {self.type_of} with name '{self.name}' is visible"):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_visible()

    def should_have_text(self, text: str, **kwargs) -> None:
        with allure.step(f"Checking that {self.type_of} with name '{self.name}' has text '{text}'"):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_text(text)
