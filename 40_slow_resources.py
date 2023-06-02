
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Slow Resources")
    ))
    link.click()

    content = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#content > div > p")
    ))
    if (content.text == 'At times it can take a while for third-party site resources to load (e.g., tracking code javascript, social networking widgets, etc.). This example has a rogue GET request that takes 30 seconds to complete.'):
        print("TestPASS. Succesefully loaded page")
    else:
        print("Test FAIL. Unable to load data")

finally:
    driver.quit()
