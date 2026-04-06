from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

# Сделалил кастомное правило которе не закрывает браузер автоматически после завершения скрипта
options.add_experimental_option("detach", True)
options.add_argument("--headless")
#Режим Headless в котором браузер не открывается

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com'
driver.get(base_url)
driver.maximize_window()

user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys ('locked_out_user')
print('Username input')

#Ввели неверный пароль
password = driver.find_element(By.ID, 'password')
password.send_keys('secret_sauc')
print('Password input')

login_btn = driver.find_element(By.ID, 'login-button')
login_btn.click()
print('Login button clicked')

#Нашли окно с ошибкой и проверили его на совпадение по тексту ошибки
error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_error = error.text
assert value_error == 'Epic sadface: Username and password do not match any user in this service'
print("Сообщение корректно")

#Нашли крестик и нажали на него после чего вывели сообщение
error_btn = driver.find_element(By.XPATH, "//button[@class='error-button']")
error_btn.click()
print("Clik error button")




