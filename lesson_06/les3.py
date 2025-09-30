from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
wait = WebDriverWait(driver, 15) 
wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "#image-container img")) >= 4)
images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

if len(images) >= 3:
        third_image = images[2]
        src_value = third_image.get_attribute("src")
        print(f"Атрибут src 3-й картинки: {src_value}")
    
driver.quit()