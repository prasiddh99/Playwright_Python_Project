import pytest
from datetime import datetime
from playwright.sync_api import sync_playwright
from utilities.test_data import BASE_URL


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store",
                     default="chrome", help="Browser Selection")


@pytest.fixture(scope="function")
def page(request):
    browser_name = request.config.getoption("browser_name")

    with sync_playwright() as p:

        # CHROME
        if browser_name == "chrome":

            browser = p.chromium.launch(headless=False, args=["--start-maximized"])

        # FIREFOX
        elif browser_name == "firefox":

            browser = p.firefox.launch(headless=False)

        # EDGE
        elif browser_name == "edge":

            browser = p.chromium.launch(channel="msedge", headless=False, args=["--start-maximized"])

        else:
            raise ValueError(
                "Please provide valid browser: chrome/firefox/edge")

        context = browser.new_context(no_viewport=True)

        page = context.new_page()

        page.goto(BASE_URL)

        yield page

        browser.close()


# SCREENSHOT ON FAILURE
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield

    report = outcome.get_result()

    # Check if test failed
    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:
            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            screenshot_name = (
                f"screenshots/{item.name}_{timestamp}.png"
            )

            page.screenshot(path=screenshot_name)

            print(
                f"\nScreenshot saved: {screenshot_name}"
            )
