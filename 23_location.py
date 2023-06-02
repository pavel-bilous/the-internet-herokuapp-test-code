from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 



profile = webdriver.FirefoxProfile()
profile.set_preference("geo.prompt.testing", True)
profile.set_preference("geo.prompt.testing.allow", True)
driver = webdriver.Firefox(firefox_profile=profile)

try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Geolocation")
    ))
    link.click()
    
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#content > div > button")
    ))
    geo = driver.find_element(By.CSS_SELECTOR, '#content > div > button')
    geo.click()
   
    wait.until(EC.presence_of_element_located(
        (By.ID, "lat-value")
    ))
    latitude = driver.find_element(By.ID, 'lat-value')

    wait.until(EC.presence_of_element_located(
        (By.ID, "long-value")
    ))
    longitude = driver.find_element(By.ID, 'long-value')

    print('Test PASS:' + latitude.text + " " + longitude.text)

finally:
    driver.quit()