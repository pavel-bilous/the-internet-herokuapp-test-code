from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import urllib3


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    chekbox_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Checkboxes")
    ))
    chekbox_link.click()
    

    for element in driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]'):
        
        isChecked = element.get_attribute("checked")
        
        if isChecked == 'true':
            element.click()
            isCheckedNew = element.get_attribute("checked")
            if isCheckedNew == None:
                print('Test PASS.Succesfully Clicked  on checkbox')
            else:
                print('click failed')
        else:
            element.click()
            isCheckedNew = element.get_attribute("checked")
            if isCheckedNew == 'true':
                print('Test PASS.Succesfully Clicked  on checkbox')
            else:
                print('click failed')
     
finally:
    driver.quit()