from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Floating Menu")
    ))
    link.click()

    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Home")))
    driver.find_element(By.LINK_TEXT, 'Home').click()
    if (driver.current_url == 'https://the-internet.herokuapp.com/floating_menu#home'):
        print('Test PASS. Succesfully clicked on Home')
    else:
        print('Test FAIL. Unbale to click on menu element')
    
    driver.execute_script("window.scrollTo(0, 200)")
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "News")))
    driver.find_element(By.LINK_TEXT, 'News').click()
    if (driver.current_url == 'https://the-internet.herokuapp.com/floating_menu#news'):
        print('Test PASS. Succesfully clicked on News')
    else:
        print('Test FAIL. Unbale to click on menu element')
    
    driver.execute_script("window.scrollTo(0, 100)")
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Contact")))
    driver.find_element(By.LINK_TEXT, 'Contact').click()
    if (driver.current_url == 'https://the-internet.herokuapp.com/floating_menu#contact'):
        print('Test PASS. Succesfully clicked on Contact')
    else:
        print('Test FAIL. Unbale to click on menu element')
    
    driver.execute_script("window.scrollTo(0, 100)")
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "About")))
    driver.find_element(By.LINK_TEXT, 'About').click()
    if (driver.current_url == 'https://the-internet.herokuapp.com/floating_menu#about'):
        print('Test PASS. Succesfully clicked on About')
    else:
        print('Test FAIL. Unbale to click on menu element')


finally:
    driver.quit()