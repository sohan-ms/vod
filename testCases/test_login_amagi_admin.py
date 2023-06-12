import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time
import allure

class Test_002_amagi_admin_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = "./TestData/LoginData.xlsx"

    @pytest.mark.sanity
    @allure.description("This test case validates the Amagi Admin Valid/Invalid User Login Functionality")
    @allure.severity(severity_level="CRITICAL")
    def test_login_amagi_admin(self, setup):
        self.logger.info("Start Test_002_amagi_admin_Login Test")
        self.logger.info("Validating Login with amagi admin user")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'amagi_admin')
        lst_status = []  # Store result in array
        for row in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.path, 'amagi_admin', row, 1)
            self.password = XLUtils.readData(self.path, 'amagi_admin', row, 2)
            self.expectation = XLUtils.readData(self.path, 'amagi_admin', row, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassWord(self.password)
            self.lp.clickLogin()
            time.sleep(7)
            self.driver.save_screenshot(".//Screenshots//" + "test_login_amagi_admin_1.png")
            current_URL = self.driver.current_url
            print(current_URL)
            exp_URL = "http://3.82.204.32:31000/manage"
            if current_URL == exp_URL:  # Login Success
                if self.expectation == 'pass':
                    self.logger.info('Test Passed with valid credentials')
                    self.lp.clickLogout()
                    lst_status.append("pass")
                elif self.expectation == 'fail':  # Login Fail
                    self.logger.info('Test Failed with valid credentials')
                    self.lp.clickLogout()
                    lst_status.append("fail")
            elif current_URL != exp_URL:  # Login Not Success
                if self.expectation == 'pass':
                    self.logger.info('Test Failed with Invalid credentials')
                    self.driver.save_screenshot(".//Screenshots//" + "test_login_amagi_admin_2.png")
                    lst_status.append("fail")
                elif self.expectation == 'fail':
                    self.logger.info('Test Passed with Invalid credentials')
                    self.driver.save_screenshot(".//Screenshots//" + "test_login_amagi_admin_3.png")
                    lst_status.append("pass")
            # print(lst_status)
        if 'fail' not in lst_status:
            self.logger.info("Test_002_amagi_admin_Login Test is Passed")
            self.driver.close()
            assert True
        else:
            self.logger.error("Test_002_amagi_admin_Login Test is Failed")
            self.driver.close()
            assert False
        self.logger.info("Test_002_amagi_admin_Login Test is Completed")