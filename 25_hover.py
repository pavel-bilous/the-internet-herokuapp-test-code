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
        (By.LINK_TEXT, "Hovers")
    ))
    link.click()
    
    a = ActionChains(driver)
    wait.until(EC.presence_of_element_located(
        (By.TAG_NAME, "img")
    ))
    
    hover = driver.find_element(By.TAG_NAME, 'img')
    hovers = driver.find_elements(By.TAG_NAME, 'img')
    #hover over element
    for hover in hovers:
        a.move_to_element(hovers[1]).perform()
    
    #identify sub menu element
    submenu = driver.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(3) > div > a")
    
    # hover over element and click
    a.move_to_element(submenu).click().perform()

    wait.until(EC.presence_of_element_located(
        (By.TAG_NAME, "h1")
    ))
    message = driver.find_element(By.TAG_NAME, 'h1')
    if (message.text == 'Not Found'):
        print('Test PASS.Hovered and clicked on item successfully')
    else:
        print('Test FAIL.Unable to complete hover and click')

finally:
    driver.quit()