import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Настройка браузера
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Переход на сайт
base_url = 'https://saucedemo.com'
driver.get(base_url)

# Авторизация
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()
print("Login sequence completed")

# Проверка URL с информативным сообщением об ошибке
current_url = driver.current_url
expected_url = 'https://saucedemo.cominventory.html'
assert current_url == expected_url, f"ОШИБКА URL: Ожидали {expected_url}, получили {current_url}"
print("URL совпал")

# Проверка заголовка страницы с сообщением об ошибке
page_title = driver.find_element(By.XPATH, "//span[@class='title']").text
assert page_title == 'Products', f"ОШИБКА ЗАГОЛОВКА: Ожидали 'Products', получили '{page_title}'"
print(f"Успешно перешли на страницу: {page_title}")

# Завершение теста
driver.quit()
