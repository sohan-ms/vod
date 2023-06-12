import time

import pytest
from pageObjects.loginPage import LoginPage
from testCases.basePage import Login
from utilities.customLogger import LogGen
from pageObjects.addUsers import AddUsers
from utilities.webdriverUtility import WebDriverUtils


class TestLogin:
    logger = LogGen.loggen()

    @pytest.mark.parametrize("username, password", Login.get_data())
    def test_login(self, setup, username, password):
        self.driver = setup
        self.driver.implicitly_wait(15)
        self.driver.get("http://3.82.204.32:31000/")
        self.lp = LoginPage(self.driver)
        self.sddsf = WebDriverUtils(self.driver)
        self.bp = Login(self.driver)
        self.lp.setUserName(username)
        self.lp.setPassWord(password)
        self.lp.clickLogin()
        self.au = AddUsers(self.driver)
        self.au.click_users()
        self.listOfEmail = []
        self.listOfEmail = self.au.email_column()
        for elem in self.listOfEmail:
            if elem.text == self.au.email:
                self.logger.info("wait_for_locator already exist")
                assert False
        else:
            self.logger.info("Creating NEW USER")
            self.au.clickAddNewUsers()
            self.au.user_details()
            self.au.select_content_partner()
            self.au.save_partner()
            wait_for_locator = self.lp.wait(15)
            if wait_for_locator is True:
                self.logger.info("wait_for_locator added successfully")
                assert True
            else:
                assert False
            time.sleep(2)
            self.lp.clickLogout()
            self.driver.close()

        # self.wdu.wait_for_element_to_click(10, locator)

        # self.driver = setup
        # self.logger.info("Verify Login Test")
        # self.lp = LoginPage(self.driver)
        # self.lp.do_login()
        # time.sleep(6)
        #
        # self.driver.implicitly_wait(15)
        # act_title = self.driver.title
        #
        # if act_title == "Amagi":
        #     assert True
        #     self.lp.clickLogout()
        #     self.logger.info("Login test is Pass")
        #     self.driver.close()
        #
        # else:
        #     self.driver.save_screenshot("..//Screenshots//" + "test_login_Failed_1.png")
        #     self.lp.clickLogout()
        #     self.logger.error("Login test is failed")
        #     self.driver.close()
        #     assert False
