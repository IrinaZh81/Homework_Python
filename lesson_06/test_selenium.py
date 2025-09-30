from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

try:
    # Используем Service для инициализации
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Открываем тестовую страницу
    driver.get("https://www.google.com")
    print("✅ Selenium работает корректно!")
    print(f"Заголовок страницы: {driver.title}")
    
    # Закрываем браузер
    driver.quit()
    
except Exception as e:
    print(f"❌ Ошибка: {e}")