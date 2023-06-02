from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Sortable Data Tables")
    ))
    link.click()

    edit = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#table1 > tbody > tr:nth-child(1) > td:nth-child(6) > a:nth-child(1)")
    ))
    edit.click()

    delete = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#table1 > tbody > tr:nth-child(1) > td:nth-child(6) > a:nth-child(2)")
    ))
    delete.click()
    print('Succesfully clicked edit and delete on first element of table')

finally:
    driver.quit()
