import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Настройка опций браузера
options: webdriver.ChromeOptions = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Инициализация драйвера
driver: webdriver.Chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Открытие сайта
base_url: str = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# Ввод имени пользователя через XPATH
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys('standard_user')
time.sleep(1)

# Ввод пароля через XPATH (поиск по всей странице через *)
password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys('secret_sauce')
time.sleep(1)

# Завершение теста и закрытие сессии
driver.quit()
