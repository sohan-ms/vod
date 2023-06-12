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
from pageObjects.mediaingest import MediaIngest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_004_media_ingest_page:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @allure.description("This test case validates the search functionality")
    @allure.severity(severity_level="NORMAL")
    def test_mediaingestpage_positve(self, setup):
        self.logger.info("Started Test_004_Add_Content_Partner Test")
        self.driver = setup
        self.driver.implicitly_wait(15)
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        # time.sleep(15)
        self.cp = AddCustomer(self.driver)
        self.cp.clickContentPartner()
        # time.sleep(7)
        current_URL = self.driver.current_url
        exp_URL='http://3.82.204.32:31000/content-partner-management'
        self.mi = MediaIngest(self.driver)
        if current_URL == exp_URL:
            self.mi.clickonpartner()
            # time.sleep(7)
            self.mi.clickonchannel()
            # time.sleep(7)
            current_media_ingest_url = self.driver.current_url
            exp_media_ingest_url = "https://cp-vod-presales.amagi.tv/media-ingest"
            if current_media_ingest_url == exp_media_ingest_url:
                print("User Landed on Media Ingest Page")
                time.sleep(5)
                t = self.mi.quickfilter()
                n = int(t)
                if n > 0:
                    text = self.mi.firsttitle()
                    print(text)
                    self.mi.searchbar()
                    time.sleep(4)
                    text1 = self.mi.firsttitle()
                    print(text1)
                    time.sleep(3)
                    if text == text1:
                        print("Test passed")
                        assert True
                    else:
                        print("Test Fail")
                        assert False
                    assert True
                else:
                    print("No titles found")
                    assert True
            else:
                print("url not matching")
                assert False
        else:
            self.logger.info("failed to select customer")
            assert False
        self.driver.close()

    @pytest.mark.sanity
    @allure.description("This test case validates the search functionality")
    @allure.severity(severity_level="NORMAL")
    def test_mediaingestpage_negative(self, setup):
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
        time.sleep(5)
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        self.mi = MediaIngest(self.driver)
        if current_URL == exp_URL:
            self.mi.clickonpartner()
            time.sleep(5)
            self.mi.clickonchannel()
            time.sleep(5)
            current_media_ingest_url = self.driver.current_url
            exp_media_ingest_url = "http://3.82.204.32:31000/media-ingest"
            if current_media_ingest_url == exp_media_ingest_url:
                print("User Landed on Media Ingest Page")
                time.sleep(4)
                t = self.mi.quickfilter()
                print(t)
                n = int(t)
                if n > 0:
                    text = self.mi.firsttitle()
                    text1 = self.mi.secondtitle()
                    print(text)
                    print(text1)
                    time.sleep(3)
                    self.mi.negative_searchbar()
                    time.sleep(4)
                    text1 = self.mi.firsttitle()
                    print(text1)
                    time.sleep(3)
                    if text != text1:
                        print("Test passed")
                        assert True
                    else:
                        assert False
                else:
                    print("No titles found")
                    assert True
        else:
            self.logger.info("failed to select customer")
            assert False
        self.driver.close()

    @pytest.mark.sanity
    @allure.description("This test case validates the Episode Type filter functionality")
    @allure.severity(severity_level="NORMAL")
    def test_mediaingest_episodefilter(self, setup):
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
        time.sleep(5)
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        self.mi = MediaIngest(self.driver)
        if current_URL == exp_URL:
            self.mi.clickonpartner()
            time.sleep(5)
            self.mi.clickonchannel()
            time.sleep(8)
            current_media_ingest_url = self.driver.current_url
            exp_media_ingest_url = "http://3.82.204.32:31000/media-ingest"
            if current_media_ingest_url == exp_media_ingest_url:
                print("User Landed on Media Manger Page")
                time.sleep(5)
                t = self.mi.quickfilter()
                print(t)
                n = int(t)
                if n > 0:
                    self.mi.filtertype()
                    self.mi.episodetypefilter()
                    self.mi.applyfilter()
                    time.sleep(5)
                    elem = self.mi.typecolumn()
                    for e in elem:
                        print(e.text)
                        if e.text == 'Episode':
                            assert True
                        else:
                            print("content not matching")
                            assert False
                else:
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
    def test_mediaingest_moviefilter(self, setup):
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
        time.sleep(5)
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        self.mi = MediaIngest(self.driver)
        if current_URL == exp_URL:
            self.mi.clickonpartner()
            time.sleep(5)
            self.mi.clickonchannel()
            time.sleep(8)
            current_media_ingest_url = self.driver.current_url
            exp_media_ingest_url = "http://3.82.204.32:31000/media-ingest"
            if current_media_ingest_url == exp_media_ingest_url:
                print("User Landed on Media Manger Page")
                time.sleep(5)
                t = self.mi.quickfilter()
                print(t)
                n = int(t)
                if n > 0:
                    self.mi.filtertype()
                    self.mi.movietypefilter()
                    self.mi.applyfilter()
                    time.sleep(5)
                    elem = self.mi.typecolumn()
                    for e in elem:
                        print(e.text)
                        if e.text == 'Movie':
                            assert True
                        else:
                            print("content not matching")
                            assert False
                else:
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
    @allure.description("This test case validates the title page ")
    @allure.severity(severity_level="NORMAL")
    def test_mediaingestpage_asset(self, setup):
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
        time.sleep(5)
        current_URL = self.driver.current_url
        exp_URL='http://3.82.204.32:31000/content-partner-management'
        self.mi = MediaIngest(self.driver)
        if current_URL == exp_URL:
            self.mi.clickonpartner()
            time.sleep(5)
            self.mi.clickonchannel()
            time.sleep(5)
            current_media_ingest_url = self.driver.current_url
            exp_media_ingest_url = "http://3.82.204.32:31000/media-ingest"
            if current_media_ingest_url == exp_media_ingest_url:
                print("User Landed on Media Ingest Page")
                time.sleep(10)
                t = self.mi.quickfilter()
                n = int(t)
                if n > 0:
                    text = self.mi.firsttitle()
                    print("first title found " + text)
                    self.mi.firsttitleclick()
                    print("clicked on the title")
                    time.sleep(10)
                    text1 = self.mi.assetname()
                    print("into the asset page and found title " + text1.lower())
                    text2 = text1.lower()
                    if text == text2:
                        time.sleep(2)
                        self.mi.closebutton()
                        print("asset matching")
                        assert True
                    else:
                        print("different asset found")
                        self.mi.closebutton()
                        assert False
                else:
                    print("No titles found")
                    assert True
            else:
                print("url not matching")
                assert False
        else:
            self.logger.info("failed to select customer")
            assert False
        self.driver.close()

    @pytest.mark.sanity
    @allure.description("This test case validates the combination of filter functionality")
    @allure.severity(severity_level="NORMAL")
    def test_mediaingest_genere(self, setup):
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
        time.sleep(5)
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        self.mi = MediaIngest(self.driver)
        if current_URL == exp_URL:
            self.mi.clickonpartner()
            time.sleep(5)
            self.mi.clickonchannel()
            time.sleep(8)
            current_media_ingest_url = self.driver.current_url
            exp_media_ingest_url = "http://3.82.204.32:31000/media-ingest"
            if current_media_ingest_url == exp_media_ingest_url:
                print("User Landed on Media Manger Page")
                time.sleep(5)
                t = self.mi.quickfilter()
                print(t)
                n = int(t)
                if n > 0:
                    self.mi.filtertype()
                    self.mi.episodetypefilter()
                    self.mi.genrefilter()
                    self.mi.genreapplyfilter()
                    df = self.mi.docfilter()
                    tf = self.mi.travelfilter()
                    cf = self.mi.cookingfilter()
                    self.mi.applyfilter()
                    time.sleep(5)
                    elem = self.mi.typecolumn()
                    genr = self.mi.genrecolumn()
                    for e in elem:
                        print(e.text)
                        if e.text == 'Episode':
                            assert True
                        else:
                            print("content not matching in Type filter")
                            assert False
                    for g in genr:
                        print(g.text)
                        if g.text == df or g.text == tf or g.text == cf:
                            assert True
                        else:
                            print("content not matching in genre filter")
                            assert False
                else:
                    print("No titles found")
                    assert True
                self.driver.close()
            else:
                print("incorrect page")
        else:
            self.logger.info("failed to select customer")
            self.driver.close()
            assert False

    '''@pytest.mark.regression
    @allure.description("This test case validates the title page ")
    @allure.severity(severity_level="NORMAL")
    def test_file_upload(self, setup):
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
        time.sleep(5)
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        self.mi = MediaIngest(self.driver)
        if current_URL == exp_URL:
            self.mi.clickonpartner1()
            time.sleep(5)
            self.mi.clickonchannel1()
            time.sleep(5)
            current_media_ingest_url = self.driver.current_url
            exp_media_ingest_url = "http://3.82.204.32:31000/media-ingest"
            if current_media_ingest_url == exp_media_ingest_url:
                print("User Landed on Media Ingest Page")
                time.sleep(10)
                self.mi.uploadbutton()
                print("uploaded file")
                self.mi.uplaodconfirmbutton()
                assert True
            else:
                print("url not matching")
                assert False
        else:
            self.logger.info("failed to select customer")
            assert False
        self.driver.close()'''
