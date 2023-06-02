from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Nested Frames")
    ))
    link.click()
    

    driver.switch_to.frame('frame-top')
    driver.switch_to.frame('frame-middle')
    content = driver.find_element(By.ID, "content")
    
    if (content.text == 'MIDDLE'):
        print('Test PASS!Succesfully verified data')
    else:
        print('Test FAIL. Unable to verify data')
finally:
    driver.quit()