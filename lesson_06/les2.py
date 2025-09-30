from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

wait = WebDriverWait(driver, 10)

input_field = wait.until(EC.presence_of_element_located((By.ID, "newButtonName")))
input_field.clear()
input_field.send_keys("SkyPro")

blue_button = driver.find_element(By.ID, "updatingButton")
blue_button.click()
    
wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro"))
    
updated_button = driver.find_element(By.ID, "updatingButton")
button_text = updated_button.text
    
print(f"Текст кнопки: {button_text}")
    
driver.quit()