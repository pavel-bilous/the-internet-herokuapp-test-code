from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
import unittest, time

class Scroll(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.base_url = "https://the-internet.herokuapp.com/infinite_scroll"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_sel(self):
        driver = self.driver
        delay = 3
        driver.get(self.base_url)
        for i in range(1,100):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
        html_source = driver.page_source

if __name__ == "__main__":
    unittest.main()




