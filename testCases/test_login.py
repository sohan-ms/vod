import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @allure.description("This test case validates the Amagi Admin User Login Functionality")
    @allure.severity(severity_level="CRITICAL")
    def test_login(self, setup):
        self.logger.info("Verify Login Test")
        self.driver = setup
        self.driver.implicitly_wait(15)
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title == "Amagi":
            assert True
            self.lp.clickLogout()
            self.logger.info("Login test is Pass")
            self.driver.close()

        else:
            self.driver.save_screenshot("..//Screenshots//"+"test_login_Failed_1.png")
            self.lp.clickLogout()
            self.logger.error("Login test is failed")
            self.driver.close()
            assert False

