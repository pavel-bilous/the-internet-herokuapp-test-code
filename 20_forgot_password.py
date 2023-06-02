from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Forgot Password")
    ))
    link.click()
    
    forgot = wait.until(EC.presence_of_element_located(
        (By.ID, "email")
    ))
    forgot.click()
    forgot.send_keys('hanuman@gmail.com')
    driver.find_element(By.ID, 'form_submit').click()
    
    driver.wait.until(EC.presence_of_element_located(
        (By.TAG_NAME, "h1")
        ))
    
    message = driver.find_element(By.TAG_NAME, 'h1')
    if (message.text == 'Internal Server Error'):
        print('Test FAIL.')
    else:
        print('Test PASS.')

finally:
    driver.quit()