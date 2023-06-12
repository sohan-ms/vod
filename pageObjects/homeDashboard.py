from selenium.common.exceptions import NoSuchElementException


class HomePage:
    contentPartner_XPATH = "//h5[text()='Content Partner']"
    platforms_XPATH = "//h5[.='Platforms']"
    users_XPATH = "//h5[.='Users']"
    manage_CLASS_NAME = "dropdown-toggle manageSelected"
    reports_XPATH = "//div[@class='navigation-reports']/child::a"
    alerts_XPATH = "//div[@class='navigation-alerts']/child::a"
    kpi_XPATH = "//div[@class='navigation-kpi']/child::a"
    button_logout_xpath = "//a[.='Logout']"
    dropdown_XPATH = "//a[@id='userDropdown']/child::span"
    search_by_XPATH = "//input[@name='searchText']"
    select_search_value = "//table/tbody/tr[1]/td[1]/div/span"

    def __init__(self, driver):
        self.driver = driver

    def click_content_partner(self):
        self.driver.find_element_by_xpath(self.contentPartner_XPATH).click()

    def click_platforms(self):
        self.driver.find_element_by_xpath(self.platforms_XPATH).click()

    def click_users(self):
        self.driver.find_element_by_xpath(self.users_XPATH).click()

    def search_value_to_select(self, customer):
        self.driver.find_element_by_xpath(self.search_by_XPATH).send_keys(customer)
        self.driver.find_element_by_xpath(self.select_search_value).click()

    def search_value_to_validate(self, customer):
        self.driver.find_element_by_xpath(self.search_by_XPATH).send_keys(customer)
        txt = self.driver.find_element_by_xpath(self.select_search_value).text
        if customer == txt:
            try:
                print("element is found")
                return True
            except NoSuchElementException:
                return False

    def click_logout(self):
        self.driver.find_element_by_id(self.dropdown_XPATH).click()
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()