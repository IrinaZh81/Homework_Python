from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChomeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChomeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

element = driver.find_element(By.CSS_SELECTOR, "#text")
element.clear() 
element.send_keys("привет, привет")
driver.find_element(By.CSS_SELECTOR,"button[type=submit]").click()

sleep(10)

driver.quit()
#print(element)

#driver.find_elements()