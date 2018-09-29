from selenium import webdriver
import unittest
import time

class FindElementByCommandsClass(unittest.TestCase):
    TEST_PATH  = "http://www.seleniumeasy.com/test/input-form-demo.html"
    #PAGE OBJECT MODEL OR POM
    input_email_xpath = "//input[@name='email']"
    input_first_name_xpath = "//input[@name='first_name']"
    input_last_name_xpath = "//input[@name='last_name']"
    input_phone_xpath = "//input[@name='phone']"
    input_address_xpath = "//input[@name='address']"
    input_city_xpath = "//input[@name='city']"
    select_stsate_xpath = "//select[@name='state']"
    input_zip_xpath = "//input[@name='zip']"
    input_website_xpath = "//input[@name='website']"
    text_area_project_description_xpath = "//textarea[@name='comment']"
    radio_hosting_yes_xpath = "//input[@type='radio'][@value='yes']"
    radio_hosting_no_xpath = "//input[@type='radio'][@value='no']"
    button_send_xpath = "//button[@type='submit']"

    #login phptravel inputs
    input_username_xpath = "//input[@name='email']"
    input_password_xpath = "//input[@name='password']"
    checkbox_remember_me_xpath ="//*[@class='iCheck-helper']"
    button_login_xpath = "//button[@type='submit']"

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
        self.driver.set_script_timeout(2)
        self.driver.set_page_load_timeout(10)
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
        array_inputs = form.find_elements_by_tag_name("input")
        print(len(array_inputs))

    #test iterate inputs in form
    def test_iterate_input_elements_inside_form(self):
        form = self.driver.find_element_by_xpath("//form[@id='contact_form']")
        #input_elements = form.find_elements_by_tag_name("input")
        input_elements = form.find_elements_by_xpath("//div[@class='input-group']/input")        
        print(len(input_elements))
        for input in input_elements:
            input.send_keys("test value")

    #test assert

    #test find element by id and send keys
    def test_sendKeys(self):
        search_field = self.driver.find_element_by_xpath(self.input_email_xpath)
        search_field.click()
        search_field.send_keys("test-email@test.com")

    #test form is valid
    def test_valid_form(self):
        self.driver.find_element_by_xpath(self.input_first_name_xpath).send_keys("Jeny")
        self.driver.find_element_by_xpath(self.input_last_name_xpath).send_keys("Ramirez")
        self.driver.find_element_by_xpath(self.input_address_xpath).send_keys("1220 Hall Ave")
        self.driver.find_element_by_xpath(self.input_city_xpath).send_keys("Las Cruces")
        self.driver.find_element_by_xpath(self.input_email_xpath).send_keys("gjrmz87@gmail.com")
        self.driver.find_element_by_xpath(self.input_phone_xpath).send_keys("3333333333")
        self.driver.find_element_by_xpath(self.input_website_xpath).send_keys("www.yahoo.com")
        self.driver.find_element_by_xpath(self.input_zip_xpath).send_keys("88005")

        button_send = self.driver.find_element_by_xpath(self.button_send_xpath)

        self.assertTrue(button_send.is_enabled())
        
    #Table exercise
    def test_tabla(self):
        self.driver.get("http://toolsqa.com/automation-practice-table/")

        sample_table = self.driver.find_element_by_xpath("//table[@class='tsc_table_s13'][@summary='Sample Table']")

        table_titles = sample_table.find_elements_by_tag_name("th")

        for title in table_titles:
            print(title.text)

    #Table test Countries column
    def test_table_countries_column(self):
        self.driver.get("http://toolsqa.com/automation-practice-table/")

        sample_table = self.driver.find_element_by_xpath("//table[@class='tsc_table_s13'][@summary='Sample Table']")

        table_rows = sample_table.find_elements_by_tag_name("tr")
        
        for row in table_rows:            
            rows_cells = row.find_elements_by_tag_name("td")

            for cell in rows_cells:
                print(cell.text)    

    def test_login_phptravels(self):

        self.driver.get("https://www.phptravels.net/admin")

        self.driver.implicitly_wait(5)        

        input_username = self.driver.find_element_by_xpath(self.input_username_xpath)

        input_username.send_keys("admin@phptravels.com")

        input_password = self.driver.find_element_by_xpath(self.input_password_xpath)

        input_password.send_keys("demoadmin")

        input_remember_me = self.driver.find_element_by_xpath(self.checkbox_remember_me_xpath)

        input_remember_me.click()

        button_login = self.driver.find_element_by_xpath(self.button_login_xpath)

        button_login.click()

        self.driver.implicitly_wait(5)

        page_title = self.driver.title

        self.assertEqual(page_title, "Dashboard")


            