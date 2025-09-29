from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChomeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChomeService(ChromeDriverManager().install()))

driver.get("https://ya.ru/")

current_title = driver.title

print(current_title)

driver.quit()