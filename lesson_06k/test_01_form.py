from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def test_form_validation():
    edge_driver_path = r"C:\Users\Irina\edgedriver_win64\msedgedriver.exe"
    
    service = EdgeService(edge_driver_path)
    driver = webdriver.Edge(service=service)
    
    wait = WebDriverWait(driver, 20)
    
    try:
        print("Открываю страницу...")
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        driver.maximize_window()
        
        print("Жду загрузки формы...")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='first-name']")))
        
        print("Заполняю форму...")
        
        first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
        first_name.clear()
        first_name.send_keys("Иван")
        
        last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
        last_name.clear()
        last_name.send_keys("Петров")
        
        address = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
        address.clear()
        address.send_keys("Ленина, 55-3")
        
        email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
        email.clear()
        email.send_keys("test@skypro.com")
        
        phone = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
        phone.clear()
        phone.send_keys("+7985899998787")
        
        zip_code = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
        zip_code.clear()
        
        city = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
        city.clear()
        city.send_keys("Москва")
        
        country = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
        country.clear()
        country.send_keys("Россия")
        
        job_position = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
        job_position.clear()
        job_position.send_keys("QA")
        
        company = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
        company.clear()
        company.send_keys("SkyPro")
        
        print("Нажимаю кнопку Submit...")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        print("Жду применения валидации...")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.zip-code.alert-danger")))
        
        zip_code_field = driver.find_element(By.CSS_SELECTOR, "div.zip-code")
        zip_code_class = zip_code_field.get_attribute("class")
        
        assert "alert-danger" in zip_code_class, "Поле Zip code должно быть подсвечено красным"
        print("✓ Поле Zip code подсвечено красным")
        
        fields_to_check = [
            "first-name",
            "last-name", 
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company"
        ]
        
        for field_name in fields_to_check:
            field = driver.find_element(By.CSS_SELECTOR, f"div.{field_name}")
            field_class = field.get_attribute("class")
            assert "alert-success" in field_class, f"Поле {field_name} должно быть подсвечено зеленым"
            print(f"✓ Поле {field_name} подсвечено зеленым")
        
        print("Все проверки пройдены успешно!")
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise
    finally:
        driver.quit()
        print("Браузер закрыт.")


if __name__ == "__main__":
    test_form_validation()