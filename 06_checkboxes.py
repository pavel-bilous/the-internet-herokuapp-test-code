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
    

     # get current status of all checkboxes
    for element in driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]'):
        print("found checkbox with status: " + str(element.get_attribute("checked")))

    # reverse checkmarks on all checkboxes
    print("attempting to reverse all checkmarks...")
    for element in driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]'):
            element.click()

    # verify reversed checkmarks
    print("getting status of all checkmarks")
        

    

    """ 
        isCheckedNew = driver.find_element(By.TAG_NAME, "input").get_attribute("false");
        print('Test PASS.Succesfully Clicked  on checkbox')
    else:
        element.click()
        isCheckedNew = driver.find_element(By.TAG_NAME, "input").get_attribute("true");
        print('Test PASS.Succesfully Clicked  on checkbox') """
     
finally:
    driver.quit()