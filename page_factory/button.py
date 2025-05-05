import allure

from page_factory.component import Component


class Button(Component):
    @property
    def type_of(self) -> str:
        return 'button'

    def double_click(self, **kwargs):
        with allure.step(f'Double clicking {self.type_of} with name "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.dblclick()
