from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.labirint.ru")

sleep(25)

search_locator = "#search-field"

search_imput = driver.find_element(By.CSS_SELECTOR, search_locator)

search_imput.send_keys("Python")
search_imput.send_keys(Keys.RETURN)