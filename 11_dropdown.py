from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import Select



driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Dropdown")
    ))
    link.click()

    dropdown = wait.until(EC.presence_of_element_located((By.ID, "dropdown")))
    dropdown.click()
    select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "dropdown"))))
    select.select_by_value('1')
    selected_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//option[@selected='selected']")))
    assert selected_option.text == "Option 1"

    dropdown = wait.until(EC.presence_of_element_located((By.ID, "dropdown")))
    dropdown.click()
    select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "dropdown"))))
    select.select_by_value('2')
    selected_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//option[@selected='selected']")))
    assert selected_option.text == "Option 2"
finally:
    driver.quit()