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
        (By.LINK_TEXT, "WYSIWYG Editor")
    ))
    link.click()



    linkFrame = wait.until(EC.presence_of_element_located(
        (By.ID, "mce_0_ifr")
    ))
 
    linkFrame.click()
    driver.switch_to.frame('mce_0_ifr')

    text = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#tinymce')
        ))
   
    text.click()
    text.send_keys('I am a machine and i know how to type text by myself')

    #center = driver.find_element(By.CSS_SELECTOR, "//button[@aria-label='Align Center']")
    #center.click()


finally:
    driver.quit()