from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from time import sleep
import requests 
from bs4 import BeautifulSoup 

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Dynamic Content")
    ))
    link.click()

    count=5
    while (count>0):
        count = count-1
        driver.refresh()
        sleep(2)
        all_divs = driver.find_elements(By.XPATH , "//div[@class='large-10 columns']")
        for div in all_divs:
            print (div.text)
            print (count)
            if div.text[count] == div.text[count-1]:
                print("STATIC text")
            else:
                print("DYNAMIC text that changed peresent on page")
    
        def getdata(url): 
            r = requests.get(url) 
            return r.text 
                
        htmldata = getdata("https://the-internet.herokuapp.com/dynamic_content") 
        soup = BeautifulSoup(htmldata, 'html.parser') 
        images_box = soup.find('div', attrs={'class': 'large-2 columns'})
        for img_item in images_box.find_all('img'):
            print(img_item['src'])
            if img_item['src'][count] == img_item['src'][count-1]:
                print("STATIC image")
            else:
                print("DYNAMIC images that changed")
  
finally:
    driver.quit()