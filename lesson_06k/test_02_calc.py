from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


def test_slow_calculator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)
    result_wait = WebDriverWait(driver, 46)
    actions = ActionChains(driver)
    
    try:
        print("Открываю страницу калькулятора...")
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        driver.maximize_window()
        
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        print("Устанавливаю задержку 45 секунд...")
        delay_field = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay"))
        )
        delay_field.clear()
        delay_field.send_keys("45")
        
        print("Выполняю операцию 7 + 8 = ...")
        
        button_7 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))
        )
        actions.move_to_element(button_7).click().perform()
        print("Нажата кнопка 7")
        
        button_plus = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))
        )
        actions.move_to_element(button_plus).click().perform()
        print("Нажата кнопка +")
        
        button_8 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))
        )
        actions.move_to_element(button_8).click().perform()
        print("Нажата кнопка 8")
        
        button_equals = wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='=']"))
        )
        actions.move_to_element(button_equals).click().perform()
        print("Нажата кнопка =")
        
        print("Ожидаю результат 15 (максимум 46 секунд)...")
        result_present = result_wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        
        result_text = driver.find_element(By.CLASS_NAME, "screen").text
        assert result_text == "15", f"Ожидался результат '15', но получен '{result_text}'"
        
        print("✓ Тест пройден: результат 15 отобразился корректно")
        
    except Exception as e:
        print(f"✗ Тест не пройден: {e}")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()