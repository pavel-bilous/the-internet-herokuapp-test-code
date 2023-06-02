from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 



driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Dynamic Loading")
    ))
    link.click()
    
    
    link1 = driver.find_element(By.LINK_TEXT, 'Example 1: Element on page that is hidden')
    link1.click()
    
    button1 = driver.find_element(By.CSS_SELECTOR,'#start > button')
    button1.click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "finish")))
    final_result = driver.find_element(By.ID, 'finish')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "finish")))
    assert final_result.text == 'Hello World!'
    
    driver.back()
    link2 = driver.find_element(By.LINK_TEXT, 'Example 2: Element rendered after the fact')
    link2.click()
    
    button2 = driver.find_element(By.CSS_SELECTOR,'#start > button')
    button2.click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "finish")))
    final_result = driver.find_element(By.ID, 'finish')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "finish")))
    assert final_result.text == 'Hello World!'

finally:
    driver.quit()