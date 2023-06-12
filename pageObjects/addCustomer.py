from utilities.XLUtils import readData


class AddCustomer:
    #Add Content Partner
    button_content_partner_xpath = "//div[@class='card-body']/child::h5[.='Content Partner']"
    button_add_new_cp_xpath = "//*[@id='addNewCP']"
    modal_tittle_text = "//h5[.='Add Content Partner']"
    inputbox_contentpartner_name = "//input[@placeholder='Search/ select partner']"
    inputbox_max_channels = "//input[@class='showBottomBorder maxHeight']"
    link_add_domain = "//div[@class='addDomain domainColor']"
    inputbox_enter_domain = "//input[@placeholder='Enter domain name']"
    input_domain_name = "contentDescription"
    save_domain = "//div[@class='saveDomain']//*[name()='svg']"
    button_submit = "//div[@class='btn btn-submit']"
    search_button_xpath = "//input[@class='form-control input']"


    file = ".//TestData/customer_details.xlsx"
    partner = readData(file, "CustomDetail", 2, 2)
    domain = readData(file, "CustomDetail", 3, 2)
    no_feed = readData(file, "CustomDetail", 4, 2)
    whitelisted_domain = readData(file, "CustomDetail", 5, 2)

    def __init__(self, driver):
        self.driver = driver

    def clickContentPartner(self):
        self.driver.find_element_by_xpath(self.button_content_partner_xpath).click()

    def search_customer(self, customer):
        self.driver.find_element_by_xpath(self.search_button_xpath).send_keys(customer)

    def clickAddNewCP(self):
        self.driver.find_element_by_xpath(self.button_add_new_cp_xpath).click()

    def setContentPartnerName(self,contentpartner):
        #self.driver.find_element_by_xpath(By.cssSelector(self.inputbox_contentpartner_name))
        self.driver.find_element_by_xpath(self.inputbox_contentpartner_name).send_keys(contentpartner)

    def send_domain_name(self, domain):
        self.driver.find_element_by_class_name(self.input_domain_name).send_keys(domain)

    def setMaxChannels(self,channels):
        self.driver.find_element_by_xpath(self.inputbox_max_channels).clear()
        self.driver.find_element_by_xpath(self.inputbox_max_channels).send_keys(channels)

    def clickAdddomain(self,domain):
        self.driver.find_element_by_xpath(self.link_add_domain).click()
        self.driver.find_element_by_xpath(self.inputbox_enter_domain).send_keys(domain)
        self.driver.find_element_by_xpath(self.save_domain).click()

    def clickonSubmit(self):
        self.driver.find_element_by_xpath(self.button_submit).click()

    def get_customer_details(self):
        self.setContentPartnerName(self.partner)
        self.setMaxChannels(self.no_feed)
        self.clickAdddomain(self.whitelisted_domain)
        self.send_domain_name(self.domain)