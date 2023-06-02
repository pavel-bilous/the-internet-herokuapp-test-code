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
        (By.LINK_TEXT, "JavaScript onload event error")
    ))
    link.click()
   
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "body > p")
    ))
   
    result = driver.find_element(By.CSS_SELECTOR, 'body > p')

    if (result.text == 'This page has a JavaScript error in the onload event. This is often a problem to using normal Javascript injection techniques.'):
        print('Test PASS!')
    else:
        print('Test FAIL. Unable to verify data')

finally:
    driver.quit()