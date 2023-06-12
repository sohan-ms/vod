import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomer import AddCustomer
from pageObjects.EditCustomer import EditCustomer
from pageObjects.searchCustomer import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import random
import string
from utilities import XLUtils
import time


class Test_003_Add_Content_Partner:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    N = 9  # Random string range
    str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

    @pytest.mark.regression
    @allure.description("This test case validates the edit content partner Functionality")
    @allure.severity(severity_level="CRITICAL")
    def test_editContentPartner(self, setup):
        self.logger.info("Started Test_004_Edit_Content_Partner Test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(20)
        self.cp = AddCustomer(self.driver)
        self.cp.clickContentPartner()
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        if current_URL == exp_URL:
            self.ep = EditCustomer(self.driver)
            self.ep.selectContentPartner()
            feed_no = self.driver.find_element_by_class_name("channelTotal").text
            fn = int(feed_no)
            initial_status = self.ep.status_details()
            self.ep.editContentPartner()
            # time.sleep(2)
            self.ep.editContentPartnerStatus()

            n = [fn - 3, fn - fn, fn]
            for numbers in n:
                self.ep.send_no_of_feeds(numbers)
                self.ep.submitContentPartner()

            self.logger.info("Edited Content Partner Successfully")
            self.driver.refresh()
            final_status = self.ep.status_details()
            print(initial_status)
            print(final_status)
            assert initial_status != final_status, "status changed "
            assert True
            time.sleep(2)
            self.lp.clickLogout()

        else:
            self.logger.error("Edit Content Partner failed")
            self.driver.save_screenshot(".//Screenshots//" + "Test_004_Edd_Content_Partner_1.png")
            assert False
        self.driver.close()

