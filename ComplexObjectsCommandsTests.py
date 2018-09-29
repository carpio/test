from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
import time

#Waits needed libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ComplexObjectsCommandsClass(unittest.TestCase):

    TEST_PATH  = "http://www.tizag.com/phpT/examples/formex.php"

    select_education_xpath = "//select[@name='education']"
    # Note: also find_element_by_name('education') can be used

    select_selenium_commands_xpath = "//select[@id='selenium_commands']"

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

    def test_iterate_options(self):
        element = self.driver.find_element_by_xpath(self.select_education_xpath)

        all_options = element.find_elements_by_tag_name("option")

        for option in all_options:
            print("Value is: %s" % option.get_attribute("value"))
            print("Text is: %s" % option.text)
            option.click()

    def test_select_element(self):
        time.sleep(3)
        select_education_element = self.driver.find_element_by_xpath(self.select_education_xpath)

        #Select(WebElement) object
        select_education = Select(select_education_element)

        select_options = select_education.options

        for option in select_options:
            print("Value is: %s" % option.get_attribute("value"))
            option.click()

    def test_select_option_by_index(self):
        time.sleep(3)
        select_education_element = self.driver.find_element_by_xpath(self.select_education_xpath)

        select_education = Select(select_education_element)

        #select_options = select_education.options
        
        select_education.select_by_index(2)

        print("Selected option value: %s" % select_education.first_selected_option.get_attribute("value"))
        
    def test_select_option_by_value(self):
        time.sleep(3)
        select_education_element = self.driver.find_element_by_xpath(self.select_education_xpath)

        select_education = Select(select_education_element)

        #select_options = select_education.options
        
        select_education.select_by_value("HighSchool")

        print("Selected option value: %s" % select_education.first_selected_option.get_attribute("value"))
        
    def test_select_option_by_text(self):
        time.sleep(3)
        select_education_element = self.driver.find_element_by_xpath(self.select_education_xpath)

        select_education = Select(select_education_element)

        #select_options = select_education.options
        
        select_education.select_by_visible_text("College")

        print("Selected option value: %s" % select_education.first_selected_option.get_attribute("value"))
        
    def test_select_deselect(self):
        time.sleep(3)
        select_education_element = self.driver.find_element_by_xpath(self.select_education_xpath)

        select_education = Select(select_education_element)

        #select_options = select_education.options
        
        select_education.select_by_index(0)
        #select_education.deselect_all()

        select_education.select_by_index(1)
        #select_education.deselect_by_index(1)

        select_education.select_by_value("College")
        #select_education.deselect_by_value("College")

        select_education.select_by_visible_text("Jr.High")

        print("Selected option value: %s" % select_education.first_selected_option.get_attribute("value"))

    def test_deselect_options(self):
        self.driver.get("http://toolsqa.com/automation-practice-form/")
        time.sleep(3)
        select_selenium_commands_element = self.driver.find_element_by_xpath(self.select_selenium_commands_xpath)

        select_selenium_commands = Select(select_selenium_commands_element)

        #select_options = select_education.options
        
        select_selenium_commands.select_by_index(0)
        select_selenium_commands.deselect_all()

        select_selenium_commands.select_by_index(1)
        select_selenium_commands.deselect_by_index(1)

        #<option>'s have no value attribute
        #select_selenium_commands.select_by_value("College")
        #select_selenium_commands.deselect_by_value("College")
        
        select_selenium_commands.select_by_visible_text("WebElement Commands")

        print("Selected option value: %s" % select_selenium_commands.first_selected_option.get_attribute("value"))

    def test_wait_1(self):
        self.driver.get("http://toolsqa.com/automation-practice-switch-windows/")
        time.sleep(5)
        try:
            element = WebDriverWait(self.driver, 45).until(
                EC.text_to_be_present_in_element((By.ID, "clock"), "Buzz Buzz")
            )
        finally:
            print("Element found!")

    def test_custom_wait(self):
        self.driver.get("http://toolsqa.com/automation-practice-switch-windows/")
        
        self.driver.implicitly_wait(3)

        wait = WebDriverWait(self.driver, 15)

        is_present = wait.until(element_has_style((By.ID, "colorVar")))

        print(is_present)

class element_has_style(object):
    def __init__(self, locator):
        self.locator = locator
        #self.attribute = attribute

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if element.get_attribute("style") == "color: red;":
            return True
        else:
            return False



    