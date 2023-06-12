import time
import pytest
import allure

from pageObjects.addUsers import AddUsers
from pageObjects.contentPartners import Content_partners
from pageObjects.loginPage import LoginPage
from utilities.customLogger import LogGen


class Test_005_Add_User:
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @allure.description("This test case validates the add User Functionality")
    @allure.severity(severity_level="CRITICAL")
    def test_add_users(self, setup):
        self.logger.info("Started Test_005_Add_Users Test")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.do_login()
        self.au = AddUsers(self.driver)
        self.cp = Content_partners(self.driver)
        self.au.click_users()
        self.listOfEmail = []
        self.listOfEmail = self.au.email_column()
        for elem in self.listOfEmail:
            if elem.text == self.au.email:
                self.logger.info("email already exist")
                assert False
        else:
            self.logger.info("Creating NEW USER")
            self.au.clickAddNewUsers()
            self.au.user_details()
            self.au.select_content_partner()
            self.au.save_partner()
            wait_for_locator = self.lp.wait(15)
            if wait_for_locator is True:
                self.logger.info("user added successfully")
                assert True
            else:
                assert False
            time.sleep(2)
            self.lp.clickLogout()
            self.driver.close()
