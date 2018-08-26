from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import unittest

class TestBase(unittest.TestCase):
    driver = None

    #URL to test (global variable)
    TEST_PATH  = "http://store.demoqa.com/"

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()

        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--test-type')

        # Chrome executable path
        options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

        # chromedriver executable path
        cls.driver = webdriver.Chrome("C:/Users/GLORIAJENIFFERRAMIRE/Downloads/chromedriver_win32/chromedriver.exe",chrome_options=options)

        cls.openPage(cls.TEST_PATH)

    @classmethod
    def tearDownClass(cls):
        return cls.driver.quit()

    @classmethod
    def openPage(cls, url):
        url = cls.TEST_PATH + url
        cls.driver.get(url)
