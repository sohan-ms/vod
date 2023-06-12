import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EditPlatform:
    content_partner = "(//span[.='Testcustomer'])[2]"
    # feed = "//div[text()='Amagi    test   amagi    test']/../../td/*[name()='svg']"
    # feed = "//div[text()='Feedtest']/../../td/*[name()='svg']"
    platform_dropdown_XPATH = "//*[name()='rect' and contains(@width,'12')]"
    edit_platform_icon = "(//*[name()='svg'])[16]"
    get_platform_status_XPATH = "//div[normalize-space()='Status*']/parent::div/descendant::div[@class='columnType']/div"
    check_connection_XPATH = "//div[@class='testConnection connectionVerified']"
    click_input_tab = "//div[normalize-space()='Input']"
    input_tab_connections_XPATH = "//table/tbody/tr/td/div[@class='verifiedConnection Verified']"
    click_output_tab = "//div[normalize-space()='Output']"
    output_tab_connections_XPATH = "//table/tbody/tr/td/div[@class='verifiedConnection Verified']"
    alerts_tab_XPATH = "//div[.='Alerts']"
    sla_duration_in_input_XPATH = "//td[contains(text(),'hrs')]"
    select_sla_duration_CLASS_NAME = "selectType"
    status_in_input_XPATH = "//td[contains(text(),'ctive')]"
    edit_Alerts_XPATH = "(//div[@class='buttons']//*[name()='svg'])[2]"
    send_email_xpath = "//div[@class='domainContainer']/following::input[@placeholder='Enter domain name']"
    select_sla_hours = "(//div[@class='dropdown-menu show']/child::div[not(contains(@class,'optionSelected'))])[2]"
    select_sla_hours_XPATH = "(//div[@class='dropdown-menu show']/child::div[not(contains(@class,'optionSelected'))])[2]"
    auto_retry_checkbox_XPATH = "//div[@class='columnType alertsColumn autoRetry']//div[2]//*[name()='svg']"
    save_alert_email = "//div[@class='saveDomain']//*[name()='svg']"
    edit_alert_status_XPATH = "//div[@class='columnStatus alerts']/descendant::span[@class='slider round']"
    save_alerts_button_CLASS_NAME = "done"
    add_email_id_XPATH = "//div[.='Add email id' and @class='addDomain domainColor']"
    delete_email_XPATH = "//div[@class='domainCrossIcon']//*[name()='svg']"
    distribution_tab_XPATH = "//a[normalize-space()='DISTRIBUTION']"
    close_edit_platform = "(//div[@class='buttons']//*[name()='svg'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def edit_platform(self):
        self.driver.find_element_by_xpath(self.content_partner).click()
        # self.driver.find_element_by_xpath(self.feed).click()
        self.driver.find_element_by_xpath(self.platform_dropdown_XPATH).click()
        self.driver.find_element_by_xpath(self.edit_platform_icon).click()
        time.sleep(5)

    def connection_verify(self):
        txt = self.driver.find_element_by_xpath(self.check_connection_XPATH).text
        return txt

    def alert_status_details(self):
        txt = self.driver.find_element_by_xpath(self.edit_alert_status_XPATH).text
        return txt

    def platform_status_details(self):
        txt = self.driver.find_element_by_xpath(self.get_platform_status_XPATH).text
        return txt

    def input_tab(self):
        self.driver.find_element_by_xpath(self.click_input_tab).click()

    def get_connections_list(self):
        connections_list = self.driver.find_elements_by_xpath(self.input_tab_connections_XPATH)
        for i in connections_list:
            print(i.text)

    def output_tab(self):
        self.driver.find_element_by_xpath(self.click_output_tab).click()

    def input_alerts_tab(self):
        self.driver.find_element_by_xpath(self.alerts_tab_XPATH).click()

    def validate_sla(self):
        txt = self.driver.find_element_by_xpath(self.sla_duration_in_input_XPATH).text
        return txt

    def validate_status(self):
        txt = self.driver.find_element_by_xpath(self.status_in_input_XPATH).text
        return txt

    def edit_alerts_tab(self):
        self.driver.find_element_by_xpath(self.edit_Alerts_XPATH).click()

    def click_alerts_status(self):
        self.driver.find_element_by_xpath(self.edit_alert_status_XPATH).click()

    def auto_retry(self):
        self.driver.find_element_by_xpath(self.auto_retry_checkbox_XPATH).click()

    def set_sla_duration(self):
        self.driver.find_element_by_class_name(self.select_sla_duration_CLASS_NAME).click()
        self.driver.find_element_by_xpath(self.select_sla_hours_XPATH).click()

    def add_alert_email_address(self, email):
        self.driver.find_element_by_xpath(self.add_email_id_XPATH).click()
        self.driver.find_element_by_xpath(self.send_email_xpath).send_keys(email)
        self.driver.find_element_by_xpath(self.save_alert_email).click()

    def save_alert(self):
        self.driver.find_element_by_class_name(self.save_alerts_button_CLASS_NAME).click()

    def close_platform(self):
        self.driver.find_element_by_xpath(self.close_edit_platform).click()
