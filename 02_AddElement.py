from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

BUTTONS_ADDED_COUNT = 5

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    add_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Add/Remove Elements")
        ))
    add_link.click()
    

    add_button = wait.until(EC.presence_of_element_located
        ((By.CSS_SELECTOR, 'button')
        ))
    
    count = 5
    while (count >0):
        add_button.click()
        count = count-1

    new_buttons = driver.find_elements(By.CLASS_NAME,'added-manually')
    print(f'There was  {len(new_buttons)} new buttons elements')
    
    assert len(new_buttons) == BUTTONS_ADDED_COUNT
        
    for b in new_buttons:
        b.click()
        new_buttons = driver.find_elements(By.CLASS_NAME,'added-manually')
        print(f'There was  {len(new_buttons)}  buttons left')
    
    assert len(new_buttons) == 0
   
finally:
    driver.quit()