from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChomeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChomeService(ChromeDriverManager().install()))
driver.get("https://ya.ru/")

driver.maximize_window() #развернуть окно под размер экрана
driver.minimize_window() #свернуть окно
driver.fullscreen_window() #развернуть окно на весь экран (аналог клавиши F11)
driver.set_window_size(1000, 600)

sleep(10)