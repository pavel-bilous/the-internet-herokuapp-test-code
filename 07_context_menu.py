from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    chekbox_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Context Menu")
    ))
    chekbox_link.click()

    element = driver.find_element(By.ID, 'hot-spot')
    action = ActionChains(driver)
    action.context_click(element).perform()
    a = Alert(driver)
    a = driver.switch_to.alert
    if (a.text == 'You selected a context menu'):
        print('Test PASS. Right click succesfull')
    else:
        print('Test FAIL. Right click unsuccesfull')
    a.accept()

finally:
    driver.quit()