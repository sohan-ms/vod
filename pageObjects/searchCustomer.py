from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as  EC
from selenium.common.exceptions import TimeoutException
import time
import string


class SearchCustomer:
    search_box_customer_xpath = "//*[@id='listView']/div/div/div/div[2]/div[2]/div/input"

    def __init__(self, driver):
        self.driver = driver

    def searchContentPartner(self, customername):
        self.driver.find_element_by_xpath(self.search_box_customer_xpath).send_keys(customername)
