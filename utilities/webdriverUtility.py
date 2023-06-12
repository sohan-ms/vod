import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriverUtils:

    def __init__(self, driver):
        self.driver = driver

    #  this method wait for given time condition, to locate the element
    def wait_for_presence_of_element(self, time, locator):
        wait = WebDriverWait(self.driver, time)
        presence = wait.until(EC.presence_of_element_located((By.XPATH, locator))).is_enabled()
        return presence

    # this method wait for given time condition, to perform click on the element
    def wait_for_element_to_click(self, times, locator):
        wait = WebDriverWait(self.driver, times)
        click = wait.until(EC.element_to_be_clickable((By.XPATH, locator))).click()
        return click

    @staticmethod
    def select_text(self,dropdown ,value):
        select = Select(dropdown)
        select.select_by_visible_text(value)
        return select

    # value should be in string for selecting from dropdown elements
    @staticmethod
    def select_value(self, dropdown, value):
        select = Select(dropdown)
        select.select_by_value(value)
        return select

    # value should be in integer for selecting from dropdown elements
    @staticmethod
    def select_index(self, dropdown, value):
        select = Select(dropdown)
        select.select_by_index(value)
        return select

    # mouse hover on the selected element
    @staticmethod
    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        return action

    # method to take screenshot
    def capture_screenshot(self, name):
        path = ".//Screenshots/"
        file_name = path+name+"--"+time.asctime().replace(":","-")+".png"
        self.driver.save_screenshot(file_name)
