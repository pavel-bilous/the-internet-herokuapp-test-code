from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Key Presses")
    ))
    link.click()
   
    wait.until(EC.presence_of_element_located(
        (By.ID, "target")
    ))
    sendit = driver.find_element(By.ID, 'target')
    sendit.click()
    sendit.send_keys('F')
    result = driver.find_element(By.ID, 'result')

    if (result.text == 'You entered: F'):
        print('Test PASS!Succesfully verified data')
    else:
        print('Test FAIL. Unable to verify data')

finally:
    driver.quit()