import time

import allure
import pytest

from pageObjects.Feed import Feed
from pageObjects.addCustomer import AddCustomer
from pageObjects.homeDashboard import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.platform import PlatformPage
from testCases.basetest import Baseclass
from utilities.webdriverUtility import WebDriverUtils


class TestIntegratePlatform(Baseclass):
    @pytest.mark.smoke
    @allure.description("This test scripts validate the ADD PLATFORM FUNCTIONALITY")
    @allure.severity(severity_level="CRITICAL")
    def test_integrate_platform(self):
        self.logger.info("Started Test PLATFORM Integration")
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.cp = AddCustomer(self.driver)
        self.pf = PlatformPage(self.driver)
        self.fd = Feed(self.driver)
        self.wdu = WebDriverUtils(self.driver)
        self.driver.implicitly_wait(20)

        self.lp.do_login()
        self.hp.click_content_partner()
        self.hp.search_value_to_select(self.fd.partner)
        # self.hp.search_value_to_select("newtestfeed")
        time.sleep(5)

        # In customer configuration page
        self.pf.platform_add_button()

        # In add platform page
        self.pf.click_platform_dropdown()
        txt1 = self.driver.find_element_by_xpath("//a[.='Youtubees']").text
        self.pf.select_platform_from_list()

        time.sleep(3)
        self.wdu.wait_for_element_to_click(12, self.pf.setup_workflow_button_XPATH)
        pf_result = self.wdu.wait_for_presence_of_element(20, self.pf.setup_complete_text_XPATH)
        time.sleep(5)
        if pf_result == True:

            # Validates platform creation
            txt = self.driver.find_element_by_xpath(self.pf.get_connection_details_XPATH).text
            pf_type = self.driver.find_element_by_xpath(self.pf.delivery_type_XPATH).text
            print("connection details --", txt, " and pf type--", pf_type)

            time.sleep(3)

            # Switch to input tab
            self.pf.input_tab()
            input_name = self.pf.input_name_list()
            connection = self.pf.input_connections_list()
            for i in range(0, len(input_name)):
                input_list = input_name[i].text
                connection_list = connection[i].text
                self.logger.info(str(input_list) + " ==== " + str(connection_list))
            time.sleep(4)

            # Switch to output tab
            self.pf.output_tab()
            input_name = self.pf.input_name_list()
            connection = self.pf.input_connections_list()
            for i in range(0, len(input_name)):
                input_list = input_name[i].text
                connection_list = connection[i].text
                self.logger.info(str(input_list) + " ==== " + str(connection_list))
            time.sleep(3)

            # Switch to alert tab
            self.pf.alert_tab()
            ingestion = self.pf.alert_connections_list()
            for inge in ingestion:
                self.logger.info(str(inge.text))

            # Switch to distribution alerts tab
            self.pf.alert_distribution_tab()
            distribution = self.pf.alert_connections_list()
            for dist in distribution:
                self.logger.info(str(dist.text))

            self.pf.close_platform()
            time.sleep(4)
            self.driver.find_element_by_xpath("//div/div/*[name()='svg' and @class = 'downArrow']").click()
            txt = self.driver.find_element_by_xpath("//div[@class='platformTitleContent']").text
            pf2_type = self.driver.find_element_by_xpath("//th[.='DELIVERY TYPE']/../../../*/*/td[6]").text
            assert txt1 == txt
            assert pf_type == pf2_type

        else:
            self.wdu.capture_screenshot(self.__class__.__name__)
            self.logger.info("Integrating platform is failed")
            assert False
