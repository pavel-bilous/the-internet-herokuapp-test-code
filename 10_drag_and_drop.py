from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()


class DragTest(unittest.TestCase):
 
    def setUp(self):
        wait = WebDriverWait(driver, 10)
        self.driver = webdriver.Firefox()
    def test_drag_drop(self):
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/drag_and_drop')
        source1 = driver.find_element(By.ID, 'column-a')
        target1 = driver.find_element(By.ID, 'column-b')
        actions2 = ActionChains(driver)
        actions2.click_and_hold(source1).move_to_element(target1).pause(2).release().perform()
        print("Dragging & dropping test case successful\n")
        time.sleep(5)
        self.assertEqual("B", target1.text)
        time.sleep(2)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
  
