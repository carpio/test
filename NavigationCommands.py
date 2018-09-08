from selenium import webdriver
import unittest

class NavigationCommandsClass(unittest.TestCase):

     #URL to test (global variable)
    TEST_PATH  = "http://store.demoqa.com"
    
    def setUp(self):
        options = webdriver.ChromeOptions()

        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--test-type')

        # Chrome executable path
        options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

        # chromedriver executable path
        self.driver = webdriver.Chrome("C:/Users/GLORIAJENIFFERRAMIRE/Downloads/chromedriver_win32/chromedriver.exe",chrome_options=options)

        self.openPage("/")
        
   
    def tearDown(self):
        return self.driver.quit()
    
    def openPage(self, url):
        url = self.TEST_PATH + url
        self.driver.get(url)

    #test Page Source
    def test_pageSource(self):
        driver = self.driver
        html = driver.page_source
        print(html)

    #test title
    def test_title(self):
        driver = self.driver
        title = driver.title
        print(title)

    #test navigate, back and forward
    def test_navigateBack(self):
        driver = self.driver
        self.openPage("/products-page/product-category/")
        driver.back()
        driver.forward()

    #test find_element_by_id
    def test_findElementById(self):
        driver = self.driver
        elementoHTML = driver.find_element_by_id("menu-item-72")

        texto = elementoHTML.text

        print(texto)

    #test find_element_by_name
    def test_findElementByName(self):
        driver = self.driver
        url = "http://www.tizag.com/phpT/examples/formex.php"
        driver.get(url)

        education = driver.find_element_by_name("education")

        valor = education.get_attribute("value")
        print(valor)

    #test find_element_by_xpath

    #test send_keys



# if __name__ == '__main__':
#     unittest.main()