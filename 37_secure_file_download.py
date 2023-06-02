from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Secure File Download")
    ))
    link.click()
    
    
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys('admin' + Keys.TAB + 'admin')
    
    print('Test FAIL. No driver available that supports Prompts wth user and paswword functionality')
finally:
    driver.quit()