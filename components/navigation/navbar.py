from playwright.sync_api import Page

from page_factory.link import Link
from page_factory.list_item import ListItem


class Navbar:
    def __init__(self, page: Page):
        self.page = page

        self.dashboard_link = Link(page, locator='a[ui-sref="dashboard"]', name="Dashboard")
        self.channels_list_item = ListItem(
            page,
            locator="//a[@ng-if='value.name && value.menu.children'][normalize-space()='Channels']",
            name="Channels"
        )
        self.channels_link = Link(page, locator='a[ui-sref="clientChannel.dashboard"]', name="Channels")
        self.all_sources_link = Link(page, locator='a[ui-sref="clientChannel.allSources"]', name="All Sources")
        self.advertisers_link = Link(page, locator='a[ui-sref="clientAdvertiser.dashboard"]', name="Advertisers")
        self.all_advertisers_link = Link(
            page,
            locator='a[ui-sref="clientAdvertiser.allCampaigns"]',
            name="All Advertisers")
        self.outstream_link = Link(page, locator='a[ui-sref="outstream"]', name="Outstream")
        self.reports_link = Link(page, locator='a[ui-sref="report.view"]', name="Reports")
        self.scoring_report_link = Link(page, locator='a[ui-sref="scoringReport"]', name="Scoring report")
        self.hosted_creatives_link = Link(page, locator='a[ui-sref="hostedCreativesReport"]', name="Hosted Creatives")
        self.subid_reports_link = Link(page, locator='a[ui-sref="subIdReport"]', name="SubID reports")
        self.templated_reports_link = Link(page, locator='a[ui-sref="templatedReport"]', name="Templated reports")
        self.connections_link = Link(page, locator='a[ui-sref="waterfalls"]', name="Connections")
        self.mass_actions_link = Link(page, locator='a[ui-sref="connectionMassAction"]', name="Mass actions")
        self.global_lists_link = Link(page, locator='a[ui-sref="globalList"]', name="Global lists")
        self.Segments_link = Link(page, locator='a[ui-sref="segments"]', name="Segments")
        self.scoring_services_link = Link(page, locator='a[ui-sref="scoring"]', name="Scoring services")
        self.vmap_link = Link(page, locator='a[ui-sref="vmap"]', name="VMAP")

        self.settings_link = Link(page, locator='a[ui-sref="profile"]', name="Settings")
        self.knowledge_base_link = Link(page, locator='knowledge-base', name="Knowledge base")
        self.logout_link = Link(page, locator='a[uib-tooltip="Logout"]', name="Logout")

    def visit_dashboard(self):
        self.dashboard_link.click()

    def hover_channels_list_item(self):
        self.channels_list_item.hover()

    def visit_channels(self):
        self.channels_link.click()

    def visit_all_sources(self):
        self.all_sources_link.click()

    def visit_advertisers(self):
        self.advertisers_link.click()

    def visit_all_advertisers(self):
        self.all_advertisers_link.click()

    def visit_outstream(self):
        self.outstream_link.click()

    def visit_reports(self):
        self.reports_link.click()

    def visit_scoring_reports(self):
        self.scoring_report_link.click()

    def visit_hosted_creatives(self):
        self.hosted_creatives_link.click()

    def visit_subid_reports(self):
        self.subid_reports_link.click()

    def visit_templated_reports(self):
        self.templated_reports_link.click()

    def visit_connections(self):
        self.connections_link.click()

    def visit_mass_actions(self):
        self.mass_actions_link.click()

    def visit_global_lists(self):
        self.global_lists_link.click()

    def visit_segments(self):
        self.Segments_link.click()

    def visit_scoring_services(self):
        self.scoring_services_link.click()

    def visit_vmap(self):
        self.vmap_link.click()

    def visit_settings(self):
        self.settings_link.click()

    def visit_knowledge_base(self):
        self.knowledge_base_link.click()

    def logout(self):
        self.logout_link.click()
