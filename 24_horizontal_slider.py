from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
actions = ActionChains(driver)
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Horizontal Slider")
    ))
    link.click()
    

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#content > div > div > input[type=range]")
    ))
    slider = driver.find_element(By.CSS_SELECTOR, '#content > div > div > input[type=range]')
    slider.click()
    actions.send_keys(Keys.ARROW_RIGHT).perform()


finally:
    driver.quit()