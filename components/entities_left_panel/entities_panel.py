from playwright.sync_api import Page

from page_factory.input import Input
from page_factory.input_group import InputGroup
from page_factory.title import Title


class EntitiesPanel:
    def __init__(self, page: Page):
        self.page = page

        self.create_channel_title = Title(page, locator="div.page-title", name="Create Channel")
        self.entities_items = InputGroup(page, locator="div.item-inner > div.input-group-wrapper", name="Entities")
        self.select_entity_input = Input(
            page,
            locator="div[ng-disabled=\"$ctrl.showSearchBlock\"]",
            name="Select Entities"
        )
        self.filtered_entities = InputGroup(
            page,
            locator="div[ng-repeat=\"item in $ctrl.channelList.items track by item.id\"]",
            name="Filtered Entities"
        )
        self.entitie_name = Title(
            page,
            locator="dynamic-tooltip[tooltip-content=\"$ctrl.channelInfo.given_name\"]",
            name="Entitie name"
        )
