from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChomeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def make_screenshot(browser):
    browser.maximize_window()
    browser.get("https://ya.ru/")
    sleep(5)

    browser.save_screenshot("./lesson_06/6ya"+browser.name+".png")
    browser.quit()

chrome = webdriver.Chrome(service=ChomeService(ChromeDriverManager().install()))
ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

make_screenshot(chrome)
make_screenshot(ff)