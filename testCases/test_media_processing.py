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
from pageObjects.mediaprocessing import MediaProcessing
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from re import search
import time


class Test_005_media_processing_page:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @allure.description("This test case validates the search functionality")
    @allure.severity(severity_level="NORMAL")
    def test_mediaprocessionpage_positive(self, setup):
        self.logger.info("Started Negative Test of media_processing_page")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.cp = AddCustomer(self.driver)
        self.cp.clickContentPartner()
        time.sleep(8)
        current_URL = self.driver.current_url
        exp_URL='http://3.82.204.32:31000/content-partner-management'
        self.mp = MediaProcessing(self.driver)
        if current_URL == exp_URL:
            self.mp.clickonpartner()
            time.sleep(8)
            self.mp.clickonchannel()
            time.sleep(7)
            self.mp.clickmediaprocessing()
            time.sleep(8)
            current_media_processing_url = self.driver.current_url
            exp_media_processing_url = "http://3.82.204.32:31000/media-processing"
            if current_media_processing_url == exp_media_processing_url:
                print("User Landed on Media processing Page")
                time.sleep(6)
                nf = self.mp.noassets()
                print(nf)
                if nf:
                    print("no assets ingested")
                    self.driver.close()
                    assert True
                else:
                    t = self.mp.quickfilter()
                    n = int(t)
                    if n > 0:
                        text = self.mp.firsttitle()
                        print(text)
                        self.mp.searchbar()
                        time.sleep(8)
                        text1 = self.mp.firsttitle()
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
    def test_mediaprocessionpage_negative(self, setup):
        self.logger.info("Started Negative Test of media_processing_page")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.cp = AddCustomer(self.driver)
        self.cp.clickContentPartner()
        time.sleep(5)
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        self.mp = MediaProcessing(self.driver)
        if current_URL == exp_URL:
            self.mp.clickonpartner()
            time.sleep(5)
            self.mp.clickonchannel()
            time.sleep(3)
            self.mp.clickmediaprocessing()
            time.sleep(8)
            current_media_processing_url = self.driver.current_url
            exp_media_processing_url = "http://3.82.204.32:31000/media-processing"
            if current_media_processing_url == exp_media_processing_url:
                print("User Landed on Media processing Page")
                time.sleep(6)
                nf = self.mp.noassets()
                print(nf)
                if nf:
                    print("no assets ingested")
                    self.driver.close()
                    assert True
                else:
                    t = self.mp.quickfilter()
                    n = int(t)
                    print(n)
                    if n > 0:
                        text = self.mp.firsttitle()
                        text2 = self.mp.secondtitle()
                        print(text)
                        print(text2)
                        self.mp.negativesearchbar()
                        time.sleep(7)
                        text1 = self.mp.firsttitle()
                        print(text1)
                        time.sleep(3)
                        if text != text1:
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
    def test_mediaprocessionpage_transcoding(self, setup):
        self.logger.info("Started Negative Test of media_processing_page")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.cp = AddCustomer(self.driver)
        self.cp.clickContentPartner()
        time.sleep(8)
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        self.mp = MediaProcessing(self.driver)
        if current_URL == exp_URL:
            self.mp.clickonpartner()
            time.sleep(8)
            self.mp.clickonchannel()
            time.sleep(3)
            self.mp.clickmediaprocessing()
            time.sleep(8)
            current_media_processing_url = self.driver.current_url
            exp_media_processing_url = "http://3.82.204.32:31000/media-processing"
            if current_media_processing_url == exp_media_processing_url:
                print("User Landed on Media processing Page")
                time.sleep(6)
                nf = self.mp.noassets()
                print(nf)
                if nf:
                    print("no assets ingested")
                    self.driver.close()
                    assert True
                else:
                    t = self.mp.quickfilter()
                    print("inside transcoding")
                    tfc = self.mp.transcodingcheck()
                    print(tfc)
                    if tfc:
                        tr = self.mp.transcodingfilter()
                        m = int(tr)
                        n = int(t)
                        print(n)
                        if n > 0 and m > 0:
                            print(m)
                            self.mp.transcodingclick()
                            time.sleep(6)
                            self.elem = []
                            count = 0
                            self.elem = self.mp.columnone()
                            print("calculating the count of asset")
                            for e in self.elem:
                                c = e.text
                                print(c)
                                count = count + 1
                            print(count)
                            if count == m:
                                print("assets matching with the count")
                                self.driver.close()
                                assert True
                            else:
                                assert False
                        else:
                            print("No titles found")
                            assert True
                    else:
                        print("no assets available in transcoding failed count is 0")
                        self.driver.close()
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
    def test_mediaprocessionpage_retranscoding(self, setup):
        self.logger.info("Started Negative Test of media_processing_page")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.cp = AddCustomer(self.driver)
        self.cp.clickContentPartner()
        time.sleep(8)
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        self.mp = MediaProcessing(self.driver)
        if current_URL == exp_URL:
            self.mp.clickonpartner()
            time.sleep(8)
            self.mp.clickonchannel()
            time.sleep(3)
            self.mp.clickmediaprocessing()
            time.sleep(8)
            current_media_processing_url = self.driver.current_url
            exp_media_processing_url = "http://3.82.204.32:31000/media-processing"
            if current_media_processing_url == exp_media_processing_url:
                print("User Landed on Media processing Page")
                time.sleep(6)
                nf = self.mp.noassets()
                print(nf)
                if nf:
                    print("no assets ingested")
                    self.driver.close()
                    assert True
                else:
                    tr = self.mp.quickfilter()
                    print("inside re transcoding")
                    tfc = self.mp.retranscodingcheck()
                    print(tfc)
                    if tfc:
                        trr = self.mp.retranscodingfilter()
                        mr = int(trr)
                        nr = int(tr)
                        print(nr)
                        if nr > 0 and mr > 0:
                            print(mr)
                            self.mp.retranscodingclick()
                            time.sleep(6)
                            self.elem = []
                            countr = 0
                            self.elem = self.mp.columnone()
                            print("calculating the count of asset")
                            for er in self.elem:
                                cr = er.text
                                print(cr)
                                countr = countr + 1
                            print(countr)
                            if countr == mr:
                                print("assets matching with the count")
                                self.driver.close()
                                assert True
                            else:
                                assert False
                        else:
                            print("No titles found")
                            assert True
                    else:
                        print("no assets available in transcoding failed count is 0")
                        self.driver.close()
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
    def test_mediaprocessionpage_transcoding_failed(self, setup):
        self.logger.info("Started Negative Test of media_processing_page")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.cp = AddCustomer(self.driver)
        self.cp.clickContentPartner()
        time.sleep(15)
        current_URL = self.driver.current_url
        exp_URL = 'http://3.82.204.32:31000/content-partner-management'
        self.mp = MediaProcessing(self.driver)
        if current_URL == exp_URL:
            self.mp.clickonpartner()
            time.sleep(8)
            self.mp.clickonchannel()
            time.sleep(3)
            self.mp.clickmediaprocessing()
            time.sleep(8)
            current_media_processing_url = self.driver.current_url
            exp_media_processing_url = "http://3.82.204.32:31000/media-processing"
            if current_media_processing_url == exp_media_processing_url:
                print("User Landed on Media processing Page")
                time.sleep(6)
                nf = self.mp.noassets()
                print(nf)
                if nf:
                    print("no assets ingested")
                    self.driver.close()
                    assert True
                else:
                    tf = self.mp.quickfilter()
                    print("inside transcoding failed")
                    tfc = self.mp.transcodingfailedcheck()
                    print(tfc)
                    if tfc:
                        trf = self.mp.transcodinfailed()
                        mf = int(trf)
                        nf = int(tf)
                        print(nf)
                        if nf > 0 and mf > 0:
                            print(mf)
                            self.mp.transcodinfailedclick()
                            time.sleep(6)
                            self.elem = []
                            countf = 0
                            self.elem = self.mp.columnone()
                            print("calculating the count of asset")
                            for ef in self.elem:
                                cf = ef.text
                                print(cf)
                                countf = countf + 1
                            print(countf)
                            if countf == mf:
                                print("assets matching with the count")
                                self.driver.close()
                                assert True
                            else:
                                assert False
                        else:
                            print("No titles found")
                            assert True
                    else:
                        print("no assets available in transcoding failed count is 0")
                        self.driver.close()
                        assert True
            else:
                print("incorrect page")
        else:
            self.logger.info("failed to select customer")
            self.driver.close()
            assert False
