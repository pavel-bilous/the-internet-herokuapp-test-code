from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BUTTONS_ADDED_COUNT = 5;

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/');
   
    add_remove_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Add/Remove Elements")
    ))

    add_remove_link.click()

    add_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button')))
    
    count = BUTTONS_ADDED_COUNT
    while (count > 0):
        add_button.click()
        count = count-1;

    new_buttons = driver.find_elements(By.CLASS_NAME, 'added-manually')
    print(f'Threre were {len(new_buttons)} new button elements')

    assert len(new_buttons) == BUTTONS_ADDED_COUNT

    for b in new_buttons:
        print("Clickin on a Delete button")
        b.click()
        new_buttons = driver.find_elements(By.CLASS_NAME, 'added-manually')
        print(f'Threre were {len(new_buttons)} button elements found on a page')

    assert len(new_buttons) == 0

finally:
    driver.quit()