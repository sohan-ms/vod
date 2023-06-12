from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
import pytest
import pytest_html
from webdriver_manager.firefox import GeckoDriverManager

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

# logger = LogGen.loggen()


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f"user-agent={user_agent}")
        options.add_argument("start-maximized")
        options.add_argument("enable-automation")
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(executable_path="./drivers/chromedriver", options=options)
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        print("Launching Chrome Browser")
        driver.maximize_window()
        driver.refresh()
        '''driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
        print("Launching Chrome Browser")
        driver.maximize_window()
        driver.refresh()'''
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
        print("Launching Firefox Browser")
        driver.maximize_window()
        driver.refresh()
    else:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        print("Launching Chrome Browser")
        driver.maximize_window()
        driver.refresh()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Generating PyTest HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Amagi On-Demand'


# It is hook for delete/Modify Environment info to HTMl Reports
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


@pytest.fixture(scope="class")
def chrome_init(request):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    options = webdriver.ChromeOptions()
    # options.headless = True
    options.add_argument(f"user-agent={user_agent}")
    chrome_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # chrome_driver = webdriver.Chrome(executable_path=".//drivers/chromedriver", options=options)
    chrome_driver.maximize_window()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


# Fixture for Firefox
@pytest.fixture(scope="class")
def driver_init(request):
    # logger.info("launching firefox browser")
    ff_driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
    ff_driver.maximize_window()
    request.cls.driver = ff_driver
    yield
    # logger.info("closing firefox browser")
    ff_driver.close()
