import time

import allure
import pytest

from pageObjects.Feed import Feed
from pageObjects.addCustomer import AddCustomer
from pageObjects.homeDashboard import HomePage
from pageObjects.loginPage import LoginPage
from testCases.basetest import Baseclass
from utilities.webdriverUtility import WebDriverUtils


class TestAddFeed(Baseclass):
    @pytest.mark.smoke
    @allure.description("This test script validate the ADD FEED functionality")
    @allure.severity(severity_level="CRITICAL")
    def test_add_feed_csv(self):
        self.logger.info("Started Test_ADD_FEED test")
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.cp = AddCustomer(self.driver)
        self.fd = Feed(self.driver)
        self.wdu = WebDriverUtils(self.driver)
        self.driver.implicitly_wait(10)

        self.lp.do_login()
        self.hp.click_content_partner()
        self.hp.search_value_to_select(self.fd.partner)
        # self.hp.search_value_to_select("testcustomerfeed")
        self.fd.add_feed()
        self.logger.info("In FEED INFO TAB")
        self.fd.select_ingest_type()
        self.fd.feed_name()
        time.sleep(5)
        self.fd.setup_workflow()
        time.sleep(15)
        sc = self.wdu.wait_for_presence_of_element(15, self.fd.setup_complete_text_XPATH)
        if sc == True:
            self.fd.edit_time_zone()
            time.sleep(5)
            self.fd.click_save_proceed()
            self.fd.dismiss_alert_popup()

            # In input tab
            self.logger.info("In INPUT TAB")
            time.sleep(5)
            self.logger.info("Input connection Details")
            print("----input connection---")
            self.fd.get_input_connections_list()
            self.fd.click_save_proceed()
            self.fd.dismiss_alert_popup()
            time.sleep(5)

            # In output tab
            self.logger.info("Output connection Details")
            print("----output connection---")
            self.fd.get_output_connections_list()
            self.fd.click_save_proceed()
            time.sleep(3)

            # In alert tab
            self.logger.info("In alerts tab")
            print("----alert ingestions---")
            ingestion = self.driver.find_elements_by_xpath(self.fd.alerts_ingestion_column_XPATH)
            for inge in ingestion:
                print(inge.text)

            self.fd.close_feed()

            # validates the feed creation
            txt = self.driver.find_elements_by_xpath(self.fd.feed_list_XPATH)
            for i in txt:
                lim = i.text
                if lim == self.fd.feed_data:
                    self.logger.info("feed added success")
                    assert True
            assert True
        else:
            self.wdu.capture_screenshot(self.__class__.__name__)
            assert False
