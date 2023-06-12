import time


class PlatformPage:
    add_button_XPATH = "//button[.='ADD NEW']"
    # add_button_XPATH = "//div[normalize-space()='AUTOCHANL']/ancestor::tr/descendant::button"
    select_platform_dropdown_XPATH = "//div[.='Search/ select platform']"
    # change platform in name in xpath
    select_platform = "//a[.='Youtubees']"
    setup_workflow_button_XPATH = "//button[.='SETUP WORKFLOW']"
    setup_complete_text_XPATH = "//div[@class='columnType setupWorkFlowSuccess']/descendant::*[name()='svg']"
    delivery_type_XPATH = "//div[.='DELIVERY TYPE*']/ancestor::div[@class='columnType']/descendant::div[@class='selected link-cls']"
    get_connection_details_XPATH = "//div[contains(text(),'END POINT URL*')]/../../div[2]"
    save_button_XPATH = "//button[.='SAVE']"
    input_tab_XPATH = "//div[contains(text(),'Input')]"
    output_tab_XPATH = "//div[contains(text(),'Output')]"
    alert_tab_XPATH = "//div[contains(text(),'Alerts')]"
    distribution_alert_XPATH = "//a[.='DISTRIBUTION']"
    input_name_list_XPATH = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]//table[1]/tbody[1]/tr/td[1]"
    connections_list_XPATH = "//table/tbody/tr/td/div[@class='verifiedConnection Verified']"

    alert_tab_connections_list_XPATH = "//div[@class='selectedBox-container']/div"
    close_platform_XPATH = "(//div[@class='buttons']//*[name()='svg'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def platform_add_button(self):
        self.driver.find_element_by_xpath(self.add_button_XPATH).click()

    def click_platform_dropdown(self):
        self.driver.find_element_by_xpath(self.select_platform_dropdown_XPATH).click()

    def select_platform_from_list(self):
        self.driver.find_element_by_xpath(self.select_platform).click()

    def click_setup_workflow(self):
        self.driver.find_element_by_xpath(self.setup_workflow_button_XPATH).click()

    def save_button(self):
        self.driver.find_element_by_xpath(self.save_button_XPATH).click()

    def input_tab(self):
        self.driver.find_element_by_xpath(self.input_tab_XPATH).click()

    def output_tab(self):
        self.driver.find_element_by_xpath(self.output_tab_XPATH).click()

    def alert_tab(self):
        self.driver.find_element_by_xpath(self.alert_tab_XPATH).click()

    def alert_distribution_tab(self):
        self.driver.find_element_by_xpath(self.distribution_alert_XPATH).click()

    def input_name_list(self):
        lst = self.driver.find_elements_by_xpath(self.input_name_list_XPATH)
        return lst

    def input_connections_list(self):
        lst = self.driver.find_elements_by_xpath(self.connections_list_XPATH)
        return lst

    def alert_connections_list(self):
        lst = self.driver.find_elements_by_xpath(self.alert_tab_connections_list_XPATH)
        return lst

    def close_platform(self):
        self.driver.find_element_by_xpath(self.close_platform_XPATH).click()