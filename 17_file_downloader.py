from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
import wget

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "File Download")
    ))
    link.click()
    
    url = 'https://the-internet.herokuapp.com/download/webdriverIO.png'
    wget.download(url, '/Users/hhhhh/Desktop/webdriverIO.png')
    print("Test PASS.Succesfully downloaded file")

    url = 'https://the-internet.herokuapp.com/download/sample.png'
    wget.download(url, '/Users/hhhhh/Desktop/sample.png')
    print("Test PASS.Succesfully downloaded file")
finally:
    driver.quit()