import os
import pytest
from playwright.sync_api import Browser, expect, Playwright

from pages.channel_creation_page import ChannelCreationPage
from pages.channels_dashboard_page import ChannelDashboardPage
from pages.dashboard_page import DashboardPage
from config import get_ui_config

AUTH_FILE = "playwright/.auth/state.json"


@pytest.fixture(scope="session", autouse=True)
def setup_auth(browser: Browser):
    if not os.path.exists(AUTH_FILE):
        page = browser.new_page()
        page.goto(get_ui_config.login_url)
        page.fill("input[name='email']", get_ui_config.email)
        page.fill("input[name='password']", get_ui_config.password)
        page.click("button[type='submit']")
        expect(page.locator("img.logo-image")).to_be_visible(timeout=10000)
        page.context.storage_state(path=AUTH_FILE)
        page.close()

    yield

    if os.path.exists(AUTH_FILE):
        os.remove(AUTH_FILE)


@pytest.fixture(scope="session")
def chromium_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=AUTH_FILE)
    page = context.new_page()
    yield page
    context.close()
    browser.close()


@pytest.fixture(scope="function")
def dashboard_page(chromium_page) -> DashboardPage:
    return DashboardPage(chromium_page)


@pytest.fixture(scope="function")
def channel_dashboard_page(chromium_page) -> ChannelDashboardPage:
    return ChannelDashboardPage(chromium_page)


@pytest.fixture(scope="function")
def channel_creation_page(chromium_page) -> ChannelCreationPage:
    return ChannelCreationPage(chromium_page)

