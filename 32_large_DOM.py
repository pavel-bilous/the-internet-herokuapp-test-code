from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Large & Deep DOM")
    ))
    link.click()
   

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "column-50")
    ))
    click = driver.find_element(By.CLASS_NAME, "column-50")
    click.click()


finally:
    driver.quit()