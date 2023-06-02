from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

    p = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p')))
    print(p.text)
    
finally:
    driver.quit()