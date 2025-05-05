from page_factory.component import Component


class UnorderedList(Component):
    @property
    def type_of(self) -> str:
        return 'unordered list'
