import os
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from brocard_project.helpers import attach_web


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='Browser for test',
        choices=['firefox', 'chrome'],
        default='chrome'
    )
    parser.addoption(
        '--browser_version',
        help='Version of browser',
        choices=['128.0', '127.0'],
        default='128.0'
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_name = request.config.getoption('--browser')
    browser_version = request.config.getoption('--browser_version')
    options = Options()

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    load_dotenv()
    remote_browser_url = os.getenv("REMOTE_BROWSER_URL")

    driver = webdriver.Remote(command_executor=f"{remote_browser_url}/wd/hub",
                              options=options)

    browser.config.base_url = "https://private.mybrocard.com/"
    browser.config.driver = driver
    browser.config.driver_options = options

    browser.config.timeout = 6.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach_web.add_screenshot(browser)
    attach_web.add_logs(browser)
    attach_web.add_html(browser)
    attach_web.add_video(browser)

    browser.quit()
