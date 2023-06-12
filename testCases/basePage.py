from webdriver_manager import driver

from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_data():
        return [
            ("asif@amagi.com", "User@321"),
            ("test@gmail.com", "User@321")
        ]

    def do_login(self):
        self.driver.implicitly_wait(15)
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
