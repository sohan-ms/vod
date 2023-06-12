import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.contentPartners import Content_partners
from utilities.XLUtils import readData


class AddUsers:
    button_users_xpath = "//h5[text()='Users']"
    button_add_new_users = "//div[.='Customer Admin']/ancestor::div[@class='card-header']/descendant::a[.='Add User']"
    inputbox_name_xpath = "//div[@class='form-group addUser']/descendant::input[@placeholder='Enter name']"
    inputbox_email="email"
    inputbox_location = "location"
    inputbox_phnumber = "phonenumber"
    click_status_xpath = "//span[@class='slider round']"
    click_contentPartner="//div[@class='dropdown1']"
    select_contentParners = "//div[@class='dropdown-menu reports1 fit-menu show']/descendant::a"
    user_save_button = "//button[.='Submit' and @class='btn btn-submit']"
    email_Lists = "//table/tbody/tr[*]/td[@class='table-email-width']"

    rand_no = random.randint(0, 1000)
    email = "User" + str(rand_no) + "@amagi.com"

    file = ".//TestData/users.xlsx"
    name = readData(file, "Sheet1", 2, 2)
    # email = readData(file, "Sheet1", 3, 2)
    location = readData(file, "Sheet1", 4, 2)
    phone = readData(file, "Sheet1", 5, 2)

    def __init__(self, driver):
        self.driver = driver

    def email_column(self):
        el = self.driver.find_elements_by_xpath(self.email_Lists)
        return el

    def click_users(self):
        self.driver.find_element_by_xpath(self.button_users_xpath).click()

    def clickAddNewUsers(self):
        self.driver.find_element_by_xpath(self.button_add_new_users).click()

    def setUserName(self, name):
        self.driver.find_element_by_xpath(self.inputbox_name_xpath).send_keys(name)

    def setEmail(self, email):
        self.driver.find_element_by_name(self.inputbox_email).send_keys(email)

    def setLocation(self, location):
        self.driver.find_element_by_name(self.inputbox_location).send_keys(location)

    def setPhoneNumber(self, phonenumber):
        self.driver.find_element_by_name(self.inputbox_phnumber).send_keys(phonenumber)

    def status(self):
        self.driver.find_element_by_xpath(self.click_status_xpath).click()

    def save_partner(self):
        self.driver.find_element_by_xpath(self.user_save_button).click()

    def user_details(self):
        self.setUserName(self.name)
        self.setEmail(self.email)
        self.setLocation(self.location)
        self.setPhoneNumber(self.phone)
        self.status()

    def select_content_partner(self):
        self.driver.find_element_by_xpath(self.click_contentPartner).click()
        content_partner = self.driver.find_elements_by_xpath(self.select_contentParners)
        # "[selecting only 5 content partners]"
        for i in range(0, 6):
            content_partner[i].click()

        # "[selecting all content partners]"
        # for checkBox in content_partner:
        #     checkBox.click()