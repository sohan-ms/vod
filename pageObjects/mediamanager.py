from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MediaManager:
    partner_name = "//span[text()='Little-Dot-Studios']"
    channel_name = "//td[@class='nameInactive']/child::div[.='Ldreals']"
    mediamanager_menu = "//a[@href='/media-manager']"
    first_title = "(//tbody/tr/td[@class='asset-info']/div)[1]"
    second_title = "(//tbody/tr/td[@class='asset-info']/div)[3]"
    search_bar = "//input[@type='text']"
    empty_title = "//div[@class='no-assets']"
    quick_filter = "//li[@class='all']/child::span"
    filter_type = "//a[text()='Type']"
    genre_filter = "//a[text()='Genre']"
    episode_type_filter = "//div[@class='option']/child::span[text()='Episode']"
    movie_type_filter = "//div[@class='option']/child::span[text()='Movie']"
    documentry_filter = "(//div[@class='option'])[3]"
    cooking_filter = "(//div[@class='option'])[4]"
    travel_filter = "(//div[@class='option'])[5]"
    apply_filter = "//button[text()='APPLY FILTERS']"
    type_column = "//tr/td[3]"
    genre_column = "//tr/td[4]"
    no_assets = "//*[contains(text(),'No assets in the Ingest Queue')]"
    close_button = "(//button[@class='close'])[2]"
    asset_name = "//p[@class='asset-info pb-3']"


    def __init__(self, driver):
        self.driver = driver

    def clickonpartner(self):
        self.driver.find_element_by_xpath(self.partner_name).click()

    def clickonchannel(self):
        self.driver.find_element_by_xpath(self.channel_name).click()

    def clickmediamanager(self):
        self.driver.find_element_by_xpath(self.mediamanager_menu).click()

    def firsttitle(self):
        text = self.driver.find_element_by_xpath(self.first_title).text
        return text

    def secondtitle(self):
        title = self.driver.find_element_by_xpath(self.second_title).text
        return title

    def searchbar(self):
        text = self.driver.find_element_by_xpath(self.first_title).text
        self.driver.find_element_by_xpath(self.search_bar).send_keys(text)

    def negative_searchbar(self):
        text = self.driver.find_element_by_xpath(self.second_title).text
        self.driver.find_element_by_xpath(self.search_bar).send_keys(text)

    def emptytitle(self):
        self.driver.find_element_by_xpath(self.empty_title)

    def quickfilter(self):
        qf = self.driver.find_element_by_xpath(self.quick_filter).text
        return qf

    def filtertype(self):
        self.driver.find_element_by_xpath(self.filter_type).click()

    def episodetypefilter(self):
        tf = self.driver.find_element_by_xpath(self.episode_type_filter).text
        self.driver.find_element_by_xpath(self.episode_type_filter).click()
        return tf

    def movietypefilter(self):
        self.driver.find_element_by_xpath(self.movie_type_filter).click()

    def genreapplyfilter(self):
        self.driver.find_element_by_xpath(self.documentry_filter).click()
        self.driver.find_element_by_xpath(self.cooking_filter).click()
        self.driver.find_element_by_xpath(self.travel_filter).click()

    def applyfilter(self):
        self.driver.find_element_by_xpath(self.apply_filter).click()

    def typecolumn(self):
        tc = self.driver.find_elements_by_xpath(self.type_column)
        return tc

    def genrecolumn(self):
        gc = self.driver.find_elements_by_xpath(self.genre_column)
        return gc

    def noassets(self):
        na = self.driver.find_element_by_xpath(self.no_assets).text
        return na

    def firsttitleclick(self):
        self.driver.find_element_by_xpath(self.first_title).click()

    def closebutton(self):
        self.driver.find_element_by_xpath(self.close_button).click()

    def assetname(self):
        an = self.driver.find_element_by_xpath(self.asset_name).text
        return an

    def genrefilter(self):
        self.driver.find_element_by_xpath(self.genre_filter).click()

    def docfilter(self):
        df = self.driver.find_element_by_xpath(self.documentry_filter).text
        return df

    def cookingfilter(self):
        cf = self.driver.find_element_by_xpath(self.cooking_filter).text
        return cf

    def travelfilter(self):
        tf = self.driver.find_element_by_xpath(self.travel_filter).text
        return tf
