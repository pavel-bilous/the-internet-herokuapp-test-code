from typing import Self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Shadow DOM")
    ))
    link.click()


    #host = driver.find_element(By.ID, 'content')
    #def shadowRoot(self): 
    #    driver.execute_script("return arguments[0].shadowRoot", host)
    #    result = self.find_element(By.CSS_SELECTOR, 'p > slot')
    #   print(result.text)

finally:
    driver.quit()
