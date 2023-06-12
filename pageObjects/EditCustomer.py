from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as  EC
from selenium.common.exceptions import TimeoutException
import time
import string


class EditCustomer:
    #select_customer_xpath = "//*[@id="cp1"]/div/span"
    select_customer_xpath = "//span[.='Testcustomer']"
    edit_customer_xpath = "//*[name()='svg']/parent::span[@class='actions']"
    edit_customer_status_xpath = "//span[@class='slider round']"
    edit_customer_submit_xpath = "//div[.='Submit']"
    no_feeds = "//input[@class='showBottomBorder maxHeight']"
    get_status_detail = "//div[.='STATUS' and @class='contentTitle']/following::div[@class='contentDescription view']"

    def __init__(self, driver):
        self.driver = driver

    def selectContentPartner(self):
        self.driver.find_element_by_xpath(self.select_customer_xpath).click()

    def editContentPartner(self):
        self.driver.find_element_by_xpath(self.edit_customer_xpath).click()

    def editContentPartnerStatus(self):
        self.driver.find_element_by_xpath(self.edit_customer_status_xpath).click()

    def submitContentPartner(self):
        self.driver.find_element_by_xpath(self.edit_customer_submit_xpath).click()

    def send_no_of_feeds(self, numbers):
        self.driver.find_element_by_xpath(self.no_feeds).clear()
        self.driver.find_element_by_xpath(self.no_feeds).send_keys(numbers)

    def status_details(self):
        status = self.driver.find_element_by_xpath("//div[.='STATUS' and @class='contentTitle']/following::div[@class='contentDescription view']").text
        return status
