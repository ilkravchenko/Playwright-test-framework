import allure

from page_factory.component import Component


class RadioButton(Component):
    @property
    def type_of(self) -> str:
        return 'radio button'

    def select_radio_button(self, value: str, **kwargs):
        with allure.step(f'Select value {value} for the {self.type_of} with name "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.get_by_label(value).check()
