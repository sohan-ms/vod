import time

import allure
import pytest

from pageObjects.addCustomer import AddCustomer
from pageObjects.homeDashboard import HomePage
from pageObjects.loginPage import LoginPage
from testCases.basetest import Baseclass
from utilities.webdriverUtility import WebDriverUtils


class TestAddContentPartner(Baseclass):

    @pytest.mark.smoke
    @allure.description("This test case validates the add User Functionality")
    @allure.severity(severity_level="CRITICAL")
    def test_add_customer(self):
        self.logger.info("Started Test_Add_Content_Partner Test")
        self.driver.implicitly_wait(15)
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.cp = AddCustomer(self.driver)
        self.wdu = WebDriverUtils(self.driver)

        self.lp.do_login()

        self.hp.click_content_partner()
        self.driver.implicitly_wait(10)
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        if current_URL == exp_URL:
            self.cp.clickAddNewCP()
            self.cp.get_customer_details()
            self.cp.clickonSubmit()
            time.sleep(7)
            self.hp.search_value_to_select(self.cp.partner)
            time.sleep(5)
            feeds_no = self.driver.find_element_by_xpath("//div[.='MAX NO OF FEEDS*']/following-sibling::div[@class='contentDescription view']").text
            domain_name = self.driver.find_element_by_xpath("//div[.='DOMAIN NAME']/following-sibling::div[@class='contentDescription view']").text

            assert domain_name == self.cp.domain
            assert int(feeds_no) == self.cp.no_feed

            self.logger.info("Added Content Partner Successfully")
            assert True
        else:
            self.logger.error("Add Content Partner failed")
            self.wdu.capture_screenshot(self.__class__.__name__)
            assert False
