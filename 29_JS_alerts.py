from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()
alert = Alert(driver)
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "JavaScript Alerts")
    ))
    link.click()
   

    a = ActionChains(driver)
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#content > div > ul > li:nth-child(1) > button")
    ))
    button1 = driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(1) > button')
    button1.click()
    driver.switch_to.alert.accept()
    result = driver.find_element(By.ID, 'result')
    if (result.text == 'You successfully clicked an alert'):
        print('Test PASS! Succesfully accepted alert')
    else:
        print('Test FAIL. Unable to verify data')
    
    button2 = driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(2) > button')
    button2.click()
    driver.switch_to.alert.accept()
    result = driver.find_element(By.ID, 'result')
    if (result.text == 'You clicked: Ok'):
        print('Test PASS! Succesfully Accepted Prompt')
    else:
        print('Test FAIL. Unable to verify data')

    button3 = driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(3) > button')
    button3.click()
    driver.switch_to.alert.send_keys('23')
    driver.switch_to.alert.accept()

    result = driver.find_element(By.ID, 'result')
    if (result.text == 'You entered: 23'):
        print('Test PASS! Succesfully send keys to alert')
    else:
        print('Test FAIL. Unable to verify data')

finally:
    driver.quit()