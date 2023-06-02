from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    ab_test = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "A/B Testing")
        ))
    ab_test.click()
    
    text_origin = "Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through)."
    text1 = wait.until(EC.text_to_be_present_in_element(By.CSS_SELECTOR, "p"))
    assert text_origin in text1.text


    driver.back()

    main_page_header  = wait.until(EC.presence_of_all_elements_located(By.CLASS_NAME, "heading"))

    main_header_text = "Welcome to the-internet"
    assert main_header_text in main_page_header.text
finally:
    driver.quit()