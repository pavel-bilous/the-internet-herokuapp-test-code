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
        
        isChecked = driver.find_element(By.TAG_NAME, "input").get_attribute("checked");
        
        if isChecked == 'true':
            element.click()
            isCheckedNew = driver.find_element(By.TAG_NAME, "input").get_attribute("false");
            print('Test PASS.Succesfully Clicked  on checkbox')
        else:
            element.click()
            isCheckedNew = driver.find_element(By.TAG_NAME, "input").get_attribute("true");
            print('Test PASS.Succesfully Clicked  on checkbox')
     
finally:
    driver.quit()