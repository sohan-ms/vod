'''
    not implemented
'''


class Content_partners:
    click_contentPartner = "//div[@class='dropdown1']"
    redbox = "//a[text()='Redbox']"
    jacksonville_jaguars = "//a[text()='Jacksonville-Jaguars']"
    Fast_Studios = "//a[text()='Fast-Studios']"

    def __init__(self, driver):
        self.driver = driver

    def click_cp(self):
        self.driver.find_element_by_xpath(self.click_contentPartner).click()

    def selectRedbox(self):
        self.driver.find_element_by_xpath(self.redbox).click()

    def selectJacksonville(self):
        self.driver.find_element_by_xpath(self.jacksonville_jaguars).click()

    def selectFastStudios(self):
        self.driver.find_element_by_xpath(self.Fast_Studios).click()
