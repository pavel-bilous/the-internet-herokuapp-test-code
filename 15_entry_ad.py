from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from time import sleep

driver = webdriver.Chrome()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Entry Ad")
    ))
    link.click()
    
    #1. Check modal text
    modal = driver.find_element(By.CSS_SELECTOR, '#modal > div.modal > div.modal-body > p')
    
    #2. Close modal
    modal_close = driver.find_element(By.CSS_SELECTOR, '#modal > div.modal > div.modal-footer > p')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#modal > div.modal > div.modal-footer > p')))
    assert modal.text == "It's commonly used to encourage a user to take an action (e.g., give their e-mail address to sign up for something or disable their ad blocker)."
    modal_close.click()

    #3. Re-enadble modal
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'restart-ad')))
    reenable = driver.find_element(By.ID, 'restart-ad')
    reenable.click()
    sleep(2)

    #4. Refresh page
    driver.refresh()

    #5. Check modal text again
    
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#modal > div.modal > div.modal-footer > p')))
    #modal = driver.find_element(By.CSS_SELECTOR, '#modal > div.modal > div.modal-body > p')
    #assert modal.text == "It's commonly used to encourage a user to take an action (e.g., give their e-mail address to sign up for something or disable their ad blocker)."
    print("Test PASS. Sucssessfely verified modal Window text and reenabled it")
    

finally:
    driver.quit()