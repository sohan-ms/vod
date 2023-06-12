import string
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.XLUtils import readData

class Feed:
    content_partner = "//span[.='Newtestfeed']"
    feed = "//div[text()='CKUFA']/../../td/*[name()='svg']"
    # feed = "//div[text()='Feedtest']/../../td/*[name()='svg']"
    add_feed_XPATH = "//button[.='ADD FEED']"
    select_csv_dropdown_XPATH = "//a[text()='Amagi CSV']"
    select_ingest_type_XPATH = "//div[@class='selectType']"
    setup_workflow_XPATH = "//button[.='SETUP WORKFLOW']"
    setup_complete_text_XPATH = "//div[@class='columnType setupWorkFlowSuccess']/descendant::*[name()='svg']"
    time_zone_XPATH = "//div[@class='selectType']"
    set_time_zone_XPATH = "//div[@class='dropdown-menu filters show']/child::div[not(@class='options optionSelected')]"
    active_status_XPATH = "//div[@class='columnStatus']/descendant::span[@class='slider round']"
    save_proceed_CLASS_NAME = "saveProceed"

    edit_input_tab_XPATH = "//*[name()='svg'and @class='metadataEdit']"
    feed_name_XPATH = "//input[@placeholder='Enter feed name']"
    edit_lang_support_XPATH = "//input[@placeholder='Search languages']"

    edit_Alerts_XPATH = "(//div[@class='buttons']//*[name()='svg'])[2]"
    select_sla_duration_CLASS_NAME = "selectType"
    select_sla_hours = "(//div[@class='dropdown-menu show']/child::div[not(contains(@class,'optionSelected'))])[2]"
    add_email_id_XPATH ="//div[.='Add email id' and @class='addDomain domainColor']"
    save_alerts_button_CLASS_NAME = "done"

    add_language_XPATH = "//a[.='Kannada - kan']"
    languages_CLASS_NAME = "dropdown-menu language show"
    send_email_xpath = "//div[@class='domainContainer']/following::input[@placeholder='Enter domain name']"
    delete_email_XPATH = "//div[@class='domainCrossIcon']//*[name()='svg']"
    save_alert_email = "//div[@class='saveDomain']//*[name()='svg']"
    dismiss_win_alerts_CLASSNAME = "toast-msg-close"
    edit_alert_status_XPATH = "//div[@class='columnStatus']/descendant::span[@class='slider round']"
    close_edit_feed = "//div[@class='buttons']//*[name()='svg']"
    input_tab_connections_XPATH = "//table/tbody/tr/td/div[@class='verifiedConnection Verified']"
    input_name_list_XPATH = "//table/tbody/tr/td[@class='inputfield']"
    output_name_list_XPATH = "//table/tbody/tr/td[@class='inputFieldName']"
    status_in_input_XPATH = "//td[contains(text(),'ctive')]"
    sla_duration_in_input_XPATH = "//td[contains(text(),'hrs')]"
    alerts_tab_XPATH = "//div[.='Alerts']"
    wait_xpath = "//span[.='EDIT ALERTS']"
    alerts_ingestion_column_XPATH = "//div[@class='selectedBox-container']/div"

    feed_list_XPATH = "//div[@class='channelSelect activeChannel']"


    file = ".//TestData/customer_details.xlsx"
    partner = readData(file, "CustomDetail", 2, 2)
    feed_data = readData(file, "CustomDetail", 2, 3)

    def __init__(self, driver):
        self.driver = driver

    def wait(self):
        wait = WebDriverWait(self.driver, 10)
        wt = wait.until(EC.presence_of_element_located((By.XPATH, self.wait_xpath))).is_displayed()
        return wt

    def add_feed(self):
        self.driver.find_element_by_xpath(self.add_feed_XPATH).click()

    def feed_name(self):
        # fn = self.driver.find_element_by_xpath(self.feed_name_XPATH).send_keys(''.join(random.choices(string.ascii_uppercase, k=5)))
        fn = self.driver.find_element_by_xpath(self.feed_name_XPATH).send_keys(self.feed_data)
        return fn

    def setup_workflow(self):
        self.driver.find_element_by_xpath(self.setup_workflow_XPATH).click()

    def select_ingest_type(self):
        self.driver.find_element_by_xpath(self.select_ingest_type_XPATH).click()
        self.driver.find_element_by_xpath(self.select_csv_dropdown_XPATH).click()

    def edit_feed(self):
        self.driver.find_element_by_xpath(self.content_partner).click()
        self.driver.find_element_by_xpath(self.feed).click()
        time.sleep(5)

    def edit_time_zone(self):
        self.driver.find_element_by_xpath(self.time_zone_XPATH).click()
        timezones = self.driver.find_elements_by_xpath(self.set_time_zone_XPATH)
        for tz in timezones:
            tz.click()
            break

    def set_status(self):
        self.driver.find_element_by_xpath(self.active_status_XPATH).click()

    def click_save_proceed(self):
        self.driver.find_element_by_class_name(self.save_proceed_CLASS_NAME).click()

    def edit_input_tab(self):
        self.driver.find_element_by_xpath(self.edit_input_tab_XPATH).click()

    def edit_language(self):
        self.driver.find_element_by_xpath(self.edit_lang_support_XPATH).click()
        self.driver.find_element_by_xpath(self.add_language_XPATH).click()
        self.driver.find_element_by_xpath(self.edit_lang_support_XPATH).click()

    def get_input_connections_list(self):
        connections_column = self.driver.find_elements_by_xpath(self.input_tab_connections_XPATH)
        input_name_column = self.driver.find_elements_by_xpath(self.input_name_list_XPATH)
        for i in range(0, len(connections_column)):
            print(input_name_column[i].text + "  ===  " + connections_column[i].text)

    def get_output_connections_list(self):
        connections_column = self.driver.find_elements_by_xpath(self.input_tab_connections_XPATH)
        output_name_column = self.driver.find_elements_by_xpath(self.output_name_list_XPATH)
        for i in range(0, len(connections_column)):
            print(output_name_column[i].text + "  ===  " + connections_column[i].text)


    def edit_alerts_tab(self):
        self.driver.find_element_by_xpath(self.edit_Alerts_XPATH).click()

    def dismiss_alert_popup(self):
        self.driver.find_element_by_class_name(self.dismiss_win_alerts_CLASSNAME).click()

    def input_alerts_tab(self):
        self.driver.find_element_by_xpath(self.alerts_tab_XPATH).click()

    def set_sla_duration(self):
        self.driver.find_element_by_class_name(self.select_sla_duration_CLASS_NAME).click()
        self.driver.find_element_by_xpath(self.select_sla_hours).click()

    def validate_sla(self):
        txt = self.driver.find_element_by_xpath(self.sla_duration_in_input_XPATH).text
        return txt

    def validate_status(self):
        txt = self.driver.find_element_by_xpath(self.status_in_input_XPATH).text
        return txt

    def add_alert_email_address(self, email):
        self.driver.find_element_by_xpath(self.add_email_id_XPATH).click()
        self.driver.find_element_by_xpath(self.send_email_xpath).send_keys(email)
        self.driver.find_element_by_xpath(self.save_alert_email).click()

    def alerts_status(self):
        self.driver.find_element_by_xpath(self.edit_alert_status_XPATH).click()

    def save_alert(self):
        self.driver.find_element_by_class_name(self.save_alerts_button_CLASS_NAME).click()

    def close_feed(self):
        self.driver.find_element_by_xpath(self.close_edit_feed).click()
