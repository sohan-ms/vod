import time

import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.addUsers import AddUsers
from pageObjects.Feed import Feed
from pageObjects.homeDashboard import HomePage
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.support import expected_conditions as EC


class Test_EditFeed:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @allure.description("This test case validates the edit Feed Functionality")
    @allure.severity(severity_level="CRITICAL")
    def test_edit_feed(self, setup):
        self.logger.info("Started Test_Edit_Feed Test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.ef = Feed(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(10)
        self.au = AddUsers(self.driver)
        self.hp = HomePage(self.driver)
        self.hp.click_content_partner()

        self.ef.edit_feed()
        self.ef.input_alerts_tab()
        self.logger.info("Landed to ALERTS TAB")
        init_sla = self.ef.validate_sla()
        init_status = self.ef.validate_status()
        self.ef.edit_alerts_tab()
        wt = self.ef.wait()
        assert wt is True, " In EDIT ALERT page"
        self.logger.info("opened EDIT ALERT page")
        self.ef.set_sla_duration()
        self.ef.add_alert_email_address(self.au.email)
        self.ef.alerts_status()
        self.ef.save_alert()
        time.sleep(4)
        final_sla = self.ef.validate_sla()
        final_status = self.ef.validate_status()

        assert init_sla != final_sla, "changed sla duration"
        assert init_status != final_status, "status changed"
        self.logger.info("edit alert successfully modified")
        self.ef.close_feed()

        self.hp.click_logout()
        self.driver.close()
