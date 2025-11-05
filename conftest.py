import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright_instance:
        # Launch Google Chrome (not generic Chromium) in headed mode for visibility
        browser = playwright_instance.chromium.launch(channel="chrome", headless=False)
        try:
            yield browser
        finally:
            browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()