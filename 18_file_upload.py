from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import requests
from time import sleep

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "File Upload")
    ))
    link.click()
    
    dfile = open("/Users/hhhhh/Desktop/sample.png", "rb")
    url = "https://the-internet.herokuapp.com/upload"
    test_res = requests.post(url, files = {"file": dfile})
    if test_res.ok:
        print(" File uploaded successfully ! ")
    else:
        print(" Please Upload again ! ")
        
    sleep(5)
finally:
    driver.quit()