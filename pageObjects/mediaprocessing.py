from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MediaProcessing:
    partner_name = "//span[text()='Tastemade_QA']"
    channel_name = "//div[text()='Tastemade-v2']"
    mediaprocessing_menu = "//a[@href='/media-processing' and @title='Media Processing']"
    quick_filter = "//li[@class='all']/child::span"
    first_title = '(//a[@href="/media-processing"])[4]'
    second_title = '(//a[@href="/media-processing"])[5]'
    search_bar = "//input[@type='text']"
    transcoding = "(//li[@class]/child::span)[2]"
    retranscoding = "(//li[@class]/child::span)[3]"
    transcoding_failed = "(//li[@class]/child::span)[4]"
    column1 = '//a[@href="/media-processing" and @class="asset-id"]'
    noassetsfound = "//p[text()='No assets ingested']"

    def __init__(self, driver):
        self.driver = driver

    def clickonpartner(self):
        self.driver.find_element_by_xpath(self.partner_name).click()

    def clickonchannel(self):
        self.driver.find_element_by_xpath(self.channel_name).click()

    def clickmediaprocessing(self):
        self.driver.find_element_by_xpath(self.mediaprocessing_menu).click()

    def quickfilter(self):
        qf = self.driver.find_element_by_xpath(self.quick_filter).text
        return qf

    def transcodingfilter(self):
        qf = self.driver.find_element_by_xpath(self.transcoding).text
        return qf

    def transcodingclick(self):
        self.driver.find_element_by_xpath(self.transcoding).click()

    def retranscodingfilter(self):
        qf = self.driver.find_element_by_xpath(self.retranscoding).text
        return qf

    def retranscodingclick(self):
        self.driver.find_element_by_xpath(self.retranscoding).click()

    def transcodinfailed(self):
        qf = self.driver.find_element_by_xpath(self.transcoding_failed).text
        return qf

    def transcodinfailedclick(self):
        self.driver.find_element_by_xpath(self.transcoding_failed).click()

    def firsttitle(self):
        text = self.driver.find_element_by_xpath(self.first_title).text
        return text

    def secondtitle(self):
        title = self.driver.find_element_by_xpath(self.second_title).text
        return title

    def searchbar(self):
        text = self.driver.find_element_by_xpath(self.first_title).text
        self.driver.find_element_by_xpath(self.search_bar).send_keys(text)

    def negativesearchbar(self):
        text = self.driver.find_element_by_xpath(self.second_title).text
        self.driver.find_element_by_xpath(self.search_bar).send_keys(text)

    def columnone(self):
        tc = self.driver.find_elements_by_xpath(self.column1)
        return tc

    def noassets(self):
        na = len(self.driver.find_elements_by_xpath(self.noassetsfound))
        print(na)
        return na

    def transcodingfailedcheck(self):
        tfc = len(self.driver.find_elements_by_xpath(self.transcoding_failed))
        print(tfc)
        return tfc

    def retranscodingcheck(self):
        tfrc = len(self.driver.find_elements_by_xpath(self.retranscoding))
        print(tfrc)
        return tfrc

    def transcodingcheck(self):
        tfcc = len(self.driver.find_elements_by_xpath(self.transcoding))
        print(tfcc)
        return tfcc
