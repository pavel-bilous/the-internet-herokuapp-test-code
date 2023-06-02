from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
actions = ActionChains(driver)
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "JQuery UI Menus")
    ))
    link.click()
    

    a = ActionChains(driver)
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Enabled')
    ))
    
    hover1 = driver.find_element(By.LINK_TEXT, 'Enabled')
    a.move_to_element(hover1).perform()


    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Downloads')
    ))
    hover2 = driver.find_element(By.LINK_TEXT, 'Downloads')
    a.move_to_element(hover2).perform()
 
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'PDF')
    ))
    hover3 = driver.find_element(By.LINK_TEXT, 'PDF')
    a.move_to_element(hover3).perform()
    hover3.click()
    
    print('YES! Assigment Complete')

finally:
    driver.quit()