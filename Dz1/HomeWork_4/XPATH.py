import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# Сделалил кастомное правило которе не закрывает браузер автоматически после завершения скрипта
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# Находим на странице поле для ввода имени c помощью кастомного типа XPATH
user_name = driver.find_element(By.ID, //input[@id='user-name'])
user_name.send_keys('standard_user') # Ввод имени в поле "usesname"
time.sleep(1) # указываем таймер паузы для проверки корректного ввода
# С помощью другого типа XPATH (*) означает что тут мы ищем по всей странице Id = 'password'
password = driver.find_element(By.ID, //*[@id='password']
password.send_keys('secret_sauce') # Ввод пароля в поле "password"
time.sleep(1) # указываем таймер паузы для проверки корректного ввода
driver.quit() # Команда для полного закрытия окна браузера
