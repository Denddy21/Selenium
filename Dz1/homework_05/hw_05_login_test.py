import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
# Сделали кастомное правило, которое не закрывает браузер автоматически
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# Находим на странице поле для ввода имени и вводим данные
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys('standard_user')
time.sleep(1)

# Ввод пароля
password = driver.find_element(By.ID, 'password')
password.send_keys('secret_sauce')

# Поиск кнопки и нажатие одним действием
driver.find_element(By.ID, 'login-button').click()

time.sleep(1)
driver.quit()
