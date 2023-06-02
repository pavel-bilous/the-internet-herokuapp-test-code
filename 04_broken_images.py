from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import urllib3


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    brokeimg_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Broken Images")
    ))
    brokeimg_link.click()
    
    imgs  = wait.until(EC.presence_of_all_elements_located(
        (By.TAG_NAME, 'img')
    ))
    
    http = urllib3.PoolManager()
    error = http.request("GET", "https://the-internet.herokuapp.com/asdf.jpg")
    if (error.status == 404):
        print("HTTP 404 ERROR")
    else:
        print("Image loaded!")

    http = urllib3.PoolManager()
    error = http.request("GET", "https://the-internet.herokuapp.com/hjkl.jpg")
    if (error.status == 404):
        print("HTTP 404 ERROR")
    else:
        print("Image loaded!")
        
    http = urllib3.PoolManager()
    error = http.request("GET", "https://the-internet.herokuapp.com/img/avatar-blank.jpg")
    if (error.status == 404):
        print("HTTP 404 ERROR")
    else:
        print("Image loaded!")

finally:
    driver.quit()