from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Notification Messages")
    ))
    link.click()
    
    
    
    result = wait.until(EC.presence_of_element_located(
        (By.ID, "flash")
    ))
    if (result.text == 'Action successful'):
        print('Test PASS!Succesfully completed actionon on the first try')
    else:
        click = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Click here")
        ))
        click.click()
        result = wait.until(EC.presence_of_element_located(
        (By.ID, "flash")
    ))
        print('Test PASS. Succesfully loaded new message: ' + result.text)
finally:
    driver.quit()