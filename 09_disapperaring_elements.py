from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Disappearing Elements")
    ))
    link.click()

    while True:
        try:
            wait = WebDriverWait(driver, 10)
            driver.find_element(By.PARTIAL_LINK_TEXT, 'Gallery')
        except NoSuchElementException:
            driver.refresh()
        else:
            driver.find_element(By.PARTIAL_LINK_TEXT, 'Gallery').click()
            print("Succesfully clicked on ghost element")

            newlink = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))

            if (newlink.text == 'Not Found'):
                print("Test PASS")
            else:
                print("Test FAIL")
            break
finally:
    driver.quit()