import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options: webdriver.ChromeOptions = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

driver: webdriver.Chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Открытие сайта
base_url: str = 'https://www.saucedemo.com'
driver.get(base_url)

# Ввод данных заблокированного пользователя
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys('locked_out_user')
print('Username input')

password = driver.find_element(By.ID, 'password')
password.send_keys('secret_sauc')
print('Password input')

# Нажатие на кнопку входа
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()
print('Login button clicked')

# Поиск и проверка текста сообщения об ошибке
error_message_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
actual_error_text = error_message_element.text
expected_error_text = 'Epic sadface: Username and password do not match any user in this service'

assert actual_error_text == expected_error_text, f"ОШИБКА: Ожидали '{expected_error_text}', но получили '{actual_error_text}'"
print("Сообщение об ошибке корректно")

# Закрытие окна ошибки через кнопку-крестик
close_error_button = driver.find_element(By.XPATH, "//button[@class='error-button']")
close_error_button.click()
print("Error message closed")

# Завершение теста
driver.quit()
