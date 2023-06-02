from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Frames")
    ))
    link.click()
    
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "iFrame")
    ))
    linkFrame = driver.find_element(By.LINK_TEXT, 'iFrame')
    linkFrame.click()
    driver.switch_to.frame('mce_0_ifr')
    
    frame = driver.find_element(By.ID, 'tinymce')
    frame.click()
    frame.send_keys('Typing  new text over here. lookslike iFrame works properly')


finally:
    driver.quit()