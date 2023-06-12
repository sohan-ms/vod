

class ReportsPage:

    reports_tab = "//a[@href='/reports']"
    reports_page_xpath = "//a[@class='dropdown-toggle manageSelected']"
    #generate_xpath="//a[@id='generateId']"
    select_content_partner_dropdown = "//div[@class='columnType']//div//div[@class='dropdown']"
    button_view_report = "//button[text()='VIEW REPORT']"
    select_feed_dropdown = "//div[text()='FEED *']/parent::div[@class='columnType ']/descendant::div[@class='selectedBox-container']"
    select_platforms_dropdown = "//div[text()='PLATFORMS *']/parent::div[@class='columnType']/descendant::div[@class='selectedBox-container']"
    date_range_start = "//input[@name='start-avail-date']"
    date_range_end = "//input[@name='end-avail-date']"
    billing_reports = "//div[text()='BILLING REPORTS']"
    save_report_button = "//div[@class='save']//button"
    yes_button = "//button[normalize-space()='Yes']"


    def __init__(self, driver):
        self.driver = driver

    def click_on_reports(self):
        self.driver.find_element_by_xpath(self.reports_tab).click()
        # self.driver.find_element_by_partial_link_text(self.reports_tab).click()


    def click_cp_dropdown(self):
        self.driver.find_element_by_xpath(self.select_content_partner_dropdown).click()

    def click_feed_dropdown(self):
        self.driver.find_element_by_xpath(self.select_feed_dropdown).click()

    def click_platform_dropdown(self):
        self.driver.find_element_by_xpath(self.select_platforms_dropdown).click()

    def view_report_button(self):
        self.driver.find_element_by_xpath(self.button_view_report).click()

    def save_button(self):
        self.driver.find_element_by_xpath(self.save_report_button).click()

    def click_yes_button(self):
        self.driver.find_element_by_xpath(self.yes_button).click()

