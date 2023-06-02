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
        (By.LINK_TEXT, "Multiple Windows")
    ))
    link.click()
    
    
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Click Here")
    ))
    click = driver.find_element(By.LINK_TEXT, "Click Here")
    click.click()

    wait.until(EC.number_of_windows_to_be(2))
    original_window = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    
    wait.until(EC.title_is("New Window"))

    wait.until(EC.presence_of_element_located(
        (By.TAG_NAME, 'h3')
    ))

    result = driver.find_element(By.TAG_NAME, 'h3')
    if (result.text == 'New Window'):
        print('Test PASS!Succesfully verified data')
    else:
        print('Test FAIL. Unable to verify data')
finally:
    driver.quit()