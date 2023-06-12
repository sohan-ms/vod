import time

import allure
import pytest

from pageObjects.addUsers import AddUsers
from pageObjects.loginPage import LoginPage
from pageObjects.reportsPage import ReportsPage
from utilities.customLogger import LogGen
from utilities.webdriverUtility import WebDriverUtils


class TestReports:

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @allure.description("This Test Script validate the REPORTS Functionality")
    @allure.severity(severity_level="CRITICAL")
    def test_reports(self, setup):
        # self.logger.info("Started TestReports Test")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.rp = ReportsPage(self.driver)
        self.wdu = WebDriverUtils(self.driver)

        self.lp.do_login()
        self.driver.implicitly_wait(10)
        time.sleep(8)
        self.rp.click_on_reports()
        self.rp.click_cp_dropdown()
        self.driver.find_element_by_xpath("//a[normalize-space()='ALCHIMIE']").click()
        time.sleep(4)
        self.rp.view_report_button()
        self.rp.save_button()
        self.rp.click_yes_button()
        get = self.driver.find_element_by_xpath("//div[.='Successfully exported to S3']").is_displayed()
        print(get)


        # cp = self.driver.find_elements_by_xpath("//div[@class='dropdown-menu show']")
        # for clk in cp:
        #     clk.click()
        #     time.sleep(5)
        #     self.rp.view_report_button()
        #     self.driver.find_element_by_xpath("//div[@class='save']//button").click()