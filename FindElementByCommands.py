from selenium import webdriver
import unittest

class FindElementByCommandsClass(unittest.TestCase):
    TEST_PATH  = "http://www.seleniumeasy.com/test/input-form-demo.html"

    def setUp(self):
        options = webdriver.ChromeOptions()

        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--test-type')

        # Chrome executable path
        options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

        # Start maximized
        options.add_argument("--start-maximized")

        # chromedriver executable path
        self.driver = webdriver.Chrome("C:/Users/GLORIAJENIFFERRAMIRE/Downloads/chromedriver_win32/chromedriver.exe",chrome_options=options)

        self.openPage("")

    def tearDown(self):
        return self.driver.quit()
    
    def openPage(self, url):
        url = self.TEST_PATH + url
        self.driver.get(url)    

    #test find element by xpath
    def test_findElementBy_xpath(self):
        form = self.driver.find_element_by_xpath("//form[@id='contact_form']")
        print(form.text)

    #test find collection or array of inputs inside form
    def test_find_input_inside_form(self):
        form = self.driver.find_element_by_xpath("//form[@id='contact_form']")
        inputs = form.find_elements_by_tag_name("input")
        print(len(inputs))

    #test iterate inputs in form
    def test_iterate_input_elements_inside_form(self):
        form = self.driver.find_element_by_xpath("//form[@id='contact_form']")
        input_elements = form.find_elements_by_tag_name("input")
        for input in input_elements:
            print(input)

    #test assert

    #test find element by id and send keys
    def test_sendKeys(self):
        search_field = self.driver.find_element_by_name("email")
        search_field.click()
        search_field.send_keys("test-email@test.com")
        

