from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    inputbox_email_name = "//input[@name='email']"
    inputbox_password_name = "password"
    button_signin_xpath = "//button[.='Sign in']"
    # button_signin = "Sign in"
    button_logout_xpath = "//a[.='Logout']"
    dropdown_id = "userDropdown"
    pop_up = "//button[@class='confirmOk']"
    locator = "toast-msg-container"

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.inputbox_email_name).clear()
        self.driver.find_element_by_xpath(self.inputbox_email_name).send_keys(username)

    def setPassWord(self, password):
        self.driver.find_element_by_name(self.inputbox_password_name).clear()
        self.driver.find_element_by_name(self.inputbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_signin_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_id(self.dropdown_id).click()
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()

    def wait(self, times):
        wait = WebDriverWait(self.driver, times)
        user = wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.locator))).is_enabled()
        return user

    def do_login(self):
        self.driver.get(self.baseURL)
        self.setUserName(self.username)
        self.setPassWord(self.password)
        self.clickLogin()
