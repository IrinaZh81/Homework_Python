from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def test_sauce_demo_purchase():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    wait = WebDriverWait(driver, 10)
    
    try:
        print("Открываю сайт магазина...")
        driver.get("https://www.saucedemo.com/")
        
        print("Авторизуюсь...")
        username_field = wait.until(
            EC.element_to_be_clickable((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")
        
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        print("Успешная авторизация")
        print("Добавляю товары в корзину...")
        
        backpack_button = wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        backpack_button.click()
        print("Добавлен Sauce Labs Backpack")
        
        tshirt_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        tshirt_button.click()
        print("Добавлен Sauce Labs Bolt T-Shirt")
        
        onesie_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        onesie_button.click()
        print("Добавлен Sauce Labs Onesie")
        print("Перехожу в корзину...")
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        
        wait.until(EC.presence_of_element_located((By.ID, "cart_contents_container")))
        checkout_button = wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
        print("Нажата кнопка Checkout")
        print("Заполняю форму...")
        
        first_name_field = wait.until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        )
        first_name_field.send_keys("Ivan")
        
        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Ivanov")
        
        postal_code_field = driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys("123456")
        
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        print("Форма заполнена, нажата кнопка Continue")
        
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        print(f"Итоговая стоимость: {total_text}")
        
        total_amount = total_text.replace("Total: $", "")
        assert total_amount == "58.29", f"Ожидалась сумма $58.29, но получена ${total_amount}"
        print("Тест пройден: итоговая сумма равна $58.29")
        
    except Exception as e:
        print(f"✗ Тест не пройден: {e}")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    test_sauce_demo_purchase()