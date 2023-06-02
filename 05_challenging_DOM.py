from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
import base64
driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Challenging DOM")
    ))
    link.click()


    answer = ""
    scripts = driver.find_elements(By.TAG_NAME ,"script")
    for script in scripts:
        focusText = script.get_attribute("innerHTML")
        if "canvas.strokeText" in focusText:
            answer = focusText[focusText.index("Answer"):focusText.index("',")]
            break
    print(answer)

finally:
    driver.quit()