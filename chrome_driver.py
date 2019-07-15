import selenium as sel
from selenium import webdriver

class ChromeDriver:
    def __init__(self,path,url,element_id,receipt_number,button_name):
        self.path = path
        self.url = url
        self.element_id = element_id
        self.button_name = button_name
        self.receipt_number = receipt_number

    def execute_chrome_driver(self):

        # initite a chrome driver
        driver = webdriver.Chrome(self.path)

        # call the url
        driver.get(self.url)

        # Find the element in the response
        receipt_id_web = driver.find_element_by_id(self.element_id)

        receipt_id_web.send_keys(self.receipt_number)

        # Find the case search button
        search_button = driver.find_element_by_name(self.button_name)

        #Click the button
        search_button.click()

        #get the html of the page
        html = driver.page_source

        # Kill the driver
        driver.quit()

        return html
