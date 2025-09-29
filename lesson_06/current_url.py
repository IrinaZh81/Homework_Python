from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChomeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChomeService(ChromeDriverManager().install()))

driver.get("https://ya.ru/")

url = driver.current_url

print(url)

driver.quit()