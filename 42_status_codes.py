from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 


driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Status Codes")
    ))
    link.click()

    get_url = driver.current_url
    if (get_url == 'https://the-internet.herokuapp.com/status_codes'):
        full_codes = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "here")
        ))
        full_codes.click()
        
        get_url = driver.current_url
        if (get_url == 'http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml'):
            print('test PASS. Sucessfully followed link')
            driver.back()
        else:
            print('Test FAIL. Unable to follow aaaaaa link')
            driver.back()
        
        code200 = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "200")
        ))
        code200.click()
        

        get_url = driver.current_url
        if (get_url == 'https://the-internet.herokuapp.com/status_codes/200'):
            print('Test PASS. Sucessfully followed link')
            driver.back()
        else:
            print('Test FAIL. Unable to follow a link')
            driver.back()
        

        code301 = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "301")
        ))
        code301.click()
        get_url = driver.current_url
        if (get_url == 'https://the-internet.herokuapp.com/status_codes/301'):
            print('Test PASS. Sucessfully followed link')
            driver.back()
        else:
            print('Test FAIL. Unable to follow a link')
            driver.back()


        code404 = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "404")
        ))
        code404.click()
        get_url = driver.current_url
        if (get_url == 'https://the-internet.herokuapp.com/status_codes/404'):
            print('Test PASS. Sucessfully followed link')
            driver.back()
        else:
            print('Test FAIL. Unable to follow a link')
            driver.back()


        code500 = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "500")
        ))
        code500.click()
        get_url = driver.current_url
        if (get_url == 'https://the-internet.herokuapp.com/status_codes/500'):
            print('Test PASS. Sucessfully followed link')
            driver.back()
        else:
            print('Test FAIL. Unable to follow a link')
            driver.back() 
    else:
        print('Test FAIL. Unable to follow a link')
    

finally:
    driver.quit()
