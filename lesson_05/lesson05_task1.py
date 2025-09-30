from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")

sleep(15)

button_class = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

button_class.click()

 



