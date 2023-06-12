import pytest
from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomer import AddCustomer
from pageObjects.mediamanager import MediaManager
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from re import search
import time


class Test_005_media_manager_page:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @allure.description("This test case validates the search functionality")
    @allure.severity(severity_level="NORMAL")
    def test_mediamanagerpage_positive(self, setup):
        self.logger.info("Started Negative Test of media_manager_page")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        time.sleep(15)
        self.cp = AddCustomer(self.driver)
        self.cp.clickContentPartner()
        time.sleep(8)
        current_URL = self.driver.current_url
        exp_URL='http://3.82.204.32:31000/content-partner-management'
        self.mm = MediaManager(self.driver)
        if current_URL == exp_URL:
            self.mm.clickonpartner()
            time.sleep(7)
            self.mm.clickonchannel()
            time.sleep(7)
            self.mm.clickmediamanager()
            time.sleep(8)
            current_media_manager_url = self.driver.current_url
            exp_media_manager_url = "http://3.82.204.32:31000/media-manager"
            if current_media_manager_url == exp_media_manager_url:
                print("User Landed on Media Manger Page")
                t = self.mm.quickfilter()
                n = int(t)
                if n > 0:
                    text = self.mm.firsttitle()
                    print(text)
                    self.mm.searchbar()
                    time.sleep(15)
                    text1 = self.mm.firsttitle()
                    print(text1)
                    time.sleep(3)
                    if text == text1:
                        print("Test passed")
                        self.driver.close()
                        assert True
                    else:
                        print("Test Fail")
                        assert False
                    assert True
                else:
                    print("No titles found")
                    assert True
            else:
                print("incorrect page")
        else:
            self.logger.info("failed to select customer")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @allure.description("This test case validates the search functionality")
    @allure.severity(severity_level="NORMAL")
    def test_mediamanagerpage_Negative(self, setup):
        self.logger.info("Started Negative Test of media_manager_page")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        time.sleep(15)
        self.cp = AddCustomer(self.driver)
        self.cp.clickContentPartner()
        time.sleep(8)
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        self.mm = MediaManager(self.driver)
        if current_URL == exp_URL:
            self.mm.clickonpartner()
            time.sleep(7)
            self.mm.clickonchannel()
            time.sleep(7)
            self.mm.clickmediamanager()
            time.sleep(8)
            current_media_manager_url = self.driver.current_url
            exp_media_manager_url = "http://3.82.204.32:31000/media-manager"
            if current_media_manager_url == exp_media_manager_url:
                print("User Landed on Media Manger Page")
                t = self.mm.quickfilter()
                n = int(t)
                if n > 0:
                    text = self.mm.firsttitle()
                    text1 = self.mm.secondtitle()
                    print(text)
                    print(text1)
                    time.sleep(3)
                    self.mm.negative_searchbar()
                    time.sleep(7)
                    text1 = self.mm.firsttitle()
                    print(text1)
                    time.sleep(3)
                    if text != text1:
                        print("Test passed")
                        self.driver.close()
                        assert True
                    else:
                        print("Test Fail")
                        assert False
                else:
                    print("No titles found")
                    assert True
            else:
                print("incorrect page")
        else:
            self.logger.info("failed to select customer")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @allure.description("This test case validates the Episode type filter functionality")
    @allure.severity(severity_level="NORMAL")
    def test_mediaingest_filters(self, setup):
        self.logger.info("Started Test_004_Add_Content_Partner Test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        time.sleep(15)
        self.cp = AddCustomer(self.driver)
        self.cp.clickContentPartner()
        time.sleep(8)
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        self.mm = MediaManager(self.driver)
        if current_URL == exp_URL:
            self.mm.clickonpartner()
            time.sleep(7)
            self.mm.clickonchannel()
            time.sleep(8)
            self.mm.clickmediamanager()
            time.sleep(8)
            current_media_manager_url = self.driver.current_url
            exp_media_manager_url = "http://3.82.204.32:31000/media-manager"
            if current_media_manager_url == exp_media_manager_url:
                print("User Landed on Media Manger Page")
                time.sleep(5)
                t = self.mm.quickfilter()
                print(t)
                n = int(t)
                if n > 0:
                    self.mm.filtertype()
                    self.mm.episodetypefilter()
                    print("filter given")
                    self.mm.applyfilter()
                    print("filter applied")
                    time.sleep(5)
                    self.elem = []
                    self.elem = self.mm.typecolumn()
                    print("searching for filtered item")
                    for e in self.elem:
                        m = e.text
                        if m == "":
                            continue
                        if m == 'Episode':
                            print(m)
                            assert True
                        else:
                            print("content not matching")
                            self.driver.close()
                            assert False
                else:
                    self.driver.close()
                    print("No titles found")
                    assert True
                self.driver.close()
            else:
                print("incorrect page")
        else:
            self.logger.info("failed to select customer")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @allure.description("This test case validates the movie type filter functionality")
    @allure.severity(severity_level="NORMAL")
    def test_mediaingest_typefilter(self, setup):
        self.logger.info("Started Test_004_Add_Content_Partner Test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        time.sleep(15)
        self.cp = AddCustomer(self.driver)
        self.cp.clickContentPartner()
        time.sleep(8)
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        self.mm = MediaManager(self.driver)
        if current_URL == exp_URL:
            self.mm.clickonpartner()
            time.sleep(8)
            self.mm.clickonchannel()
            time.sleep(8)
            self.mm.clickmediamanager()
            time.sleep(8)
            current_media_manager_url = self.driver.current_url
            exp_media_manager_url = "http://3.82.204.32:31000/media-manager"
            if current_media_manager_url == exp_media_manager_url:
                print("User Landed on Media Manger Page")
                time.sleep(10)
                t = self.mm.quickfilter()
                print(t)
                n = int(t)
                if n > 0:
                    self.mm.filtertype()
                    print("clicked on type filters")
                    self.mm.movietypefilter()
                    print("filter given")
                    self.mm.applyfilter()
                    print("filter applied")
                    time.sleep(5)
                    self.elem = []
                    self.elem = self.mm.typecolumn()
                    print("searching for filtered item")
                    for e in self.elem:
                        m = e.text
                        if m == "":
                            continue
                        if m == 'Movie':
                            print(m)
                            assert True
                        else:
                            print("content not matching")
                            self.driver.close()
                            assert False
                else:
                    self.driver.close()
                    print("No titles found")
                    assert False
                self.driver.close()
            else:
                print("incorrect page")
        else:
            self.logger.info("failed to select customer")
            self.driver.close()
#             assert False

    @pytest.mark.sanity
    @allure.description("This test case validates the title page ")
    @allure.severity(severity_level="NORMAL")
    def test_mediamanagerpage_asset(self, setup):
        self.logger.info("Started Negative Test of media_manager_page")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.cp = AddCustomer(self.driver)
        self.cp.clickContentPartner()
        time.sleep(10)
        current_URL = self.driver.current_url
        exp_URL='http://3.82.204.32:31000/content-partner-management'
        self.mm = MediaManager(self.driver)
        if current_URL == exp_URL:
            self.mm.clickonpartner()
            time.sleep(8)
            self.mm.clickonchannel()
            time.sleep(8)
            self.mm.clickmediamanager()
            time.sleep(8)
            current_media_manager_url = self.driver.current_url
            exp_media_manager_url = "http://3.82.204.32:31000/media-manager"
            if current_media_manager_url == exp_media_manager_url:
                print("User Landed on Media Manger Page")
                t = self.mm.quickfilter()
                n = int(t)
                if n > 0:
                    text = self.mm.firsttitle()
                    print("first title found " + text)
                    self.mm.firsttitleclick()
                    print("clicked on the title")
                    time.sleep(10)
                    text1 = self.mm.assetname()
                    print("into the asset page and found title " + text1)
                    text2 = text1
                    if text == text2:
                        time.sleep(2)
                        self.mm.closebutton()
                        print("asset matching")
                        self.driver.close()
                        assert True
                    else:
                        print("different asset found")
                        self.mm.closebutton()
                        assert False
                else:
                    print("No titles found")
                    assert True
            else:
                print("incorrect page")
                self.driver.close()
        else:
            self.logger.info("failed to select customer")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @allure.description("This test case validates the Episode type filter functionality")
    @allure.severity(severity_level="NORMAL")
    def test_mediaingest_combination_filter(self, setup):
        self.logger.info("Started Test_004_Add_Content_Partner Test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        time.sleep(15)
        self.cp = AddCustomer(self.driver)
        self.cp.clickContentPartner()
        time.sleep(8)
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        self.mm = MediaManager(self.driver)
        if current_URL == exp_URL:
            self.mm.clickonpartner()
            time.sleep(8)
            self.mm.clickonchannel()
            time.sleep(8)
            self.mm.clickmediamanager()
            time.sleep(8)
            current_media_manager_url = self.driver.current_url
            exp_media_manager_url = "http://3.82.204.32:31000/media-manager"
            if current_media_manager_url == exp_media_manager_url:
                print("User Landed on Media Manger Page")
                time.sleep(7)
                t = self.mm.quickfilter()
                print(t)
                n = int(t)
                if n > 0:
                    self.mm.filtertype()
                    self.mm.episodetypefilter()
                    print("Type filter given")
                    self.mm.genrefilter()
                    self.mm.genreapplyfilter()
                    df = self.mm.docfilter()
                    tf = self.mm.travelfilter()
                    cf = self.mm.cookingfilter()
                    print(df + tf + cf)
                    self.mm.applyfilter()
                    print("filter applied")
                    time.sleep(7)
                    self.elem = self.mm.typecolumn()
                    self.gner = self.mm.genrecolumn()
                    print("searching for filtered item")
                    for e in self.elem:
                        m = e.text
                        if m == "":
                            continue
                        if m == 'Episode':
                            print(m)
                            assert True
                        else:
                            print("Type content not matching")
                            self.driver.close()
                            assert False
                    for g in self.gner:
                        x = g.text
                        if x == "":
                            continue
                        if x == df or x == tf or x == cf:
                            print(x)
                            assert True
                        else:
                            print("genre content not matching")
                            assert False
                else:
                    self.driver.close()
                    print("No titles found")
                    assert True
                self.driver.close()
            else:
                print("incorrect page")
        else:
            self.logger.info("failed to select customer")
            self.driver.close()
            assert False
