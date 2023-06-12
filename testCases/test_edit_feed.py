import time
import allure
import pytest

from pageObjects.addUsers import AddUsers
from pageObjects.Feed import Feed
from pageObjects.homeDashboard import HomePage
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_EditFeed:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # @pytest.mark.skip
    @allure.description("This test case validates the edit Feed Functionality")
    @allure.severity(severity_level="CRITICAL")
    def test_edit_feed(self, setup):
        self.logger.info("Started Test_Edit_Feed Test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(10)
        self.au = AddUsers(self.driver)
        self.hp = HomePage(self.driver)

        self.hp.click_content_partner()

        self.ef = Feed(self.driver)
        self.ef.edit_feed()
        # self.ef.set_status()
        # self.ef.edit_time_zone()
        time.sleep(3)
        self.ef.click_save_proceed()
        time.sleep(2)
        self.logger.info("In Input Tab")
        self.ef.dismiss_alert_popup()
        time.sleep(3)
        self.ef.get_input_connections_list()
        current_url = self.driver.current_url
        expected_url = "http://3.82.204.32:31000/content-partner-management"
        assert expected_url == current_url, "Titles are matching"
        self.ef.edit_input_tab()
        # self.ef.edit_language()
        print("output connections")
        time.sleep(5)
        self.ef.click_save_proceed()
        self.ef.dismiss_alert_popup()
        self.ef.get_output_connections_list()
        time.sleep(3)
        self.ef.close_feed()
        self.logger.info("Test_edit_feed Test is Passed")
        self.hp.click_logout()
        self.driver.close()
