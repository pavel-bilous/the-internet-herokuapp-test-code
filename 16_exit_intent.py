from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Exit Intent")
    ))
    link.click()
    
    #e = driver.find_element(By.CSS_SELECTOR, "h3")
    #action = ActionChains(driver)
    #action.move_by_offset(60,0).perform()
    #sleep(5)
    #driver.find_element(By.CSS_SELECTOR, '#ouibounce-modal > div.modal > div.modal-footer > p').click()
    

finally:
    driver.quit()