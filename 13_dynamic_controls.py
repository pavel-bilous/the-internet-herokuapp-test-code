from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from time import sleep


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Dynamic Controls")
    ))
    link.click()
    
    
    checkbox = driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
    checkbox.click()
    remove = driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button')
    remove.click()
    if (driver.find_element(By.CSS_SELECTOR, '#checkbox').is_displayed()):
        print('Test PASS. Succesfully removed checkbox and its  not displayed')
    else:
        print('Test FAIL. Unable to remove checkbox')


    enable = driver.find_element(By.CSS_SELECTOR, '#input-example > button')
    enable.click()
    sleep(3)

    if (driver.find_element(By.TAG_NAME, 'input').is_enabled() == True):
        text = driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]')
        text.click()
        text.send_keys('I am machine doing automation here')
    else:
        print('Test FAIL. Unable to complete operation')

    disable = driver.find_element(By.CSS_SELECTOR, '#input-example > button')
    disable.click()
    sleep(3)
    if (driver.find_element(By.TAG_NAME, 'input').is_enabled() == False):
        print('TEST PASS. Sended text and disabled input field')
    else:
        print('TEST FAIL. Unable to complete opration')

finally:
    driver.quit()