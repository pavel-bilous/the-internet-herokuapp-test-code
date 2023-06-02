from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
actions = ActionChains(driver)
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Inputs")
    ))
    link.click()
    
    wait.until(EC.presence_of_element_located(
        (By.TAG_NAME, "input")
    ))
    
    iinput = driver.find_element(By.TAG_NAME, 'input')
    iinput.click()
    iinput.send_keys("3")
 

    print('YES! Successfully send keys to input field')

finally:
    driver.quit()