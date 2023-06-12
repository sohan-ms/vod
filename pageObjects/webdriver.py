from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Logww:

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.inputbox_email_name).clear()
        self.driver.find_element_by_xpath(self.inputbox_email_name).send_keys(username)