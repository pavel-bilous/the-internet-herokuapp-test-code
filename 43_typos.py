from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Typos")
    ))
    link.click()


    p1expected = "This example demonstrates a typo being introduced. It does it randomly on each page load."
    p2expected = "Sometimes you'll see a typo, other times you won't."

    i = 6
    while (i>0):
        p1 = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#content > div > p:nth-child(2)")
        ))
        
        p2 = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#content > div > p:nth-child(3)")
        ))
        
        i =i-1
    
        if (p2.text == p2expected) and (p1.text == p1expected) :
            print('Test PASS! Succesfully verified data - no typos detected')
        else:
            print('Test FAIL. Unable to verify data. Typos detected')
        
        driver.refresh()
finally:
    driver.quit()