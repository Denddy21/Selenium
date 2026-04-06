import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Настройка опций для браузера
options: webdriver.ChromeOptions = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Инициализация драйвера Chrome
driver: webdriver.Chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Открытие сайта и настройка размера окна
base_url: str = 'https://www.saucedemo.com'
driver.get(base_url)
driver.set_window_size(1920, 1080)

# Поиск поля Username, ввод текста и его последующее удаление через горячие клавиши
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys('standard_user')
print("Input Login")
time.sleep(2)

user_name.send_keys(Keys.COMMAND + 'a')  # Имитация CMD + A для выделения всего текста
time.sleep(1)
user_name.send_keys(Keys.DELETE)         # Имитация DELETE для очистки поля
print("Login field cleared")

# Поиск поля Password, ввод текста и его удаление через горячие клавиши
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys("secret_sauce")
print("Input Password")
time.sleep(1)

password.send_keys(Keys.COMMAND + 'a')   # Выделение текста в поле пароля
time.sleep(1)
password.send_keys(Keys.DELETE)          # Удаление текста
print("Password field cleared")

# Поиск кнопки Login (исправлено bnt_login -> login_button) и нажатие
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()
print("Click login button")

# Пауза перед завершением и закрытие браузера
time.sleep(1)
driver.quit()  # Используем quit для полного завершения сессии
