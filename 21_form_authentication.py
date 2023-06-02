from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Form Authentication")
    ))
    link.click()
    
    wait.until(EC.presence_of_element_located(
        (By.ID, "username")
    ))
    login = driver.find_element(By.ID, 'username')
    login.send_keys('tomsmith')
    
    wait.until(EC.presence_of_element_located(
        (By.ID, "password")
    ))
    passs = driver.find_element(By.ID, 'password')
    passs.send_keys('SuperSecretPassword!')

    button = driver.find_element(By.CSS_SELECTOR, '#login > button')
    button.click()

    message = driver.find_element(By.TAG_NAME, 'h4')
    if (message.text == 'Welcome to the Secure Area. When you are done click logout below.'):
        print('Test PASS.Login Successful')
    else:
        print('Test FAIL.Unable to complete login')

finally:
    driver.quit()