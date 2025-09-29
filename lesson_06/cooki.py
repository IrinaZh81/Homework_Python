from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChomeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChomeService(ChromeDriverManager().install()))

my_cooki = {
    'name': 'cookie_policy',
    'value': '1'
}



driver.get("https://labirint.ru")

driver.add_cookie(my_cooki) #добавление куки

driver.refresh()    #обновление страницы

sleep(10)
driver.quit()