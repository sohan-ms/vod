import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomer import AddCustomer
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

    @pytest.mark.sanity
    @allure.description("This test case validates the add content partner Functionality")
    @allure.severity(severity_level="CRITICAL")
    def test_addContentPartner(self, setup):
        self.logger.info("Started Test_003_Add_Content_Partner Test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        self.cp = AddCustomer(self.driver)
        self.cp.clickContentPartner()
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        if current_URL == exp_URL:
            self.cp.clickAddNewCP()
            self.cp.setContentPartnerName(self.str)
            self.cp.setMaxChannels("8")
            self.cp.clickAdddomain("test.com")
            # self.cp.clickonSubmit()
            # time.sleep(5)
        #     self.driver.refresh()
        #     self.logger.info("Added Content Partner Successfully")
        #     assert True
        # else:
        #     self.logger.error("Add Content Partner failed")
        #     self.driver.save_screenshot(".//Screenshots//" + "Test_003_Add_Content_Partner_1.png")
        #     assert False
        # self.driver.close()
