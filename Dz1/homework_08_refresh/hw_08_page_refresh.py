import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Настройка опций для браузера
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Инициализация драйвера Chrome
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Открытие тестируемого сайта и установка разрешения окна
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
driver.set_window_size(1920, 1080)

# Поиск поля Username через XPATH и ввод логина
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys('standard_user')
print("Input Login")

# Поиск поля Password через XPATH и ввод пароля
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys('secret_sauce')
print("Input Password")

# Поиск кнопки Login (исправлено bnt_login -> login_button) и нажатие для входа
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()
print("Click login button")

# Установка таймера ожидания перед обновлением страницы
time.sleep(5)

# Метод refresh() обновляет текущую страницу браузера, перезагружая все элементы
driver.refresh()
print("Page refreshed")

# Завершение работы
driver.quit()
