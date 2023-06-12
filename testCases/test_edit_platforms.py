import time

import pytest
import allure

from pageObjects.addUsers import AddUsers
from pageObjects.editPlatform import EditPlatform
from pageObjects.homeDashboard import HomePage
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_EditFeed:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @allure.description("This test case validates the edit platform Functionality")
    @allure.severity(severity_level="CRITICAL")
    def test_edit_feed(self, setup):
        self.logger.info("Started Test_Edit_Platform Test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(20)
        self.hp = HomePage(self.driver)
        self.ef = EditPlatform(self.driver)
        self.au = AddUsers(self.driver)

        self.hp.click_content_partner()
        self.ef.edit_platform()

        status = self.ef.platform_status_details()
        print("platform status is--> ", status)
        connection = self.ef.connection_verify()
        print("platform connection type is--> ", connection)
        self.ef.input_tab()
        print("input connections type")
        self.ef.get_connections_list()
        print("output connections type")
        self.ef.get_connections_list()
        self.ef.input_alerts_tab()
        self.logger.info("validating alerts page")
        init_sla = self.ef.validate_sla()
        init_status = self.ef.validate_status()
        self.ef.edit_alerts_tab()
        self.ef.set_sla_duration()
        self.ef.alert_status_details()
        self.ef.auto_retry()
        self.ef.add_alert_email_address(self.au.email)
        self.ef.click_alerts_status()
        self.ef.save_alert()
        time.sleep(5)
        final_sla = self.ef.validate_sla()
        final_status = self.ef.validate_status()

        assert init_sla != final_sla, "changed sla duration"
        assert init_status != final_status, "status changed"
        self.logger.info("edit alert successfully modified")
        self.ef.close_platform()

        self.hp.click_logout()
        self.driver.close()
