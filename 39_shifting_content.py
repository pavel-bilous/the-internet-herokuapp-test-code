
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Shifting Content")
    ))
    link.click()

    link1 = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Example 1: Menu Element")
    ))
    link1.click()

    sublink1 = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#content > div > p:nth-child(3) > a")
    ))
    sublink1.click()
    driver.back()

    sublink2 = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#content > div > p:nth-child(4) > a")
    ))
    sublink2.click()
    driver.back()

    sublink3 = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#content > div > p:nth-child(5) > a")
    ))
    sublink3.click()

    driver.back()
    
    driver.back()
    link2 = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Example 2: An image")
    ))
    link2.click()


finally:
    driver.quit()
