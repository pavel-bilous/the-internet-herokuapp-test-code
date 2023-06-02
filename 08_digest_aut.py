from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


driver = webdriver.Chrome()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    digest_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Digest Authentication")
    ))
    digest_link.click()

    #??????
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys('admin' + Keys.TAB + 'admin')
    #driver.execute_script("driver.switchTo().alert().sendKeys('admin' + Keys.TAB + 'admin');")
   
    p = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p')))
    if (p.text == 'Congratulations! You must have the proper credentials.'):
        print('test PASS. U saccesfully logged in')
    else:
        print("Test FAIL.Unable to log in")
finally:
    driver.quit()