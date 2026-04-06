import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options: webdriver.ChromeOptions = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver: webdriver.Chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Открытие сайта и настройка окна
base_url: str = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# Ввод логина
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys('standard_user')
time.sleep(1)

# Ввод пароля
password = driver.find_element(By.ID, 'password')
password.send_keys('secret_sauce')
time.sleep(1)

# Завершение работы
driver.quit()
