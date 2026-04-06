import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
driver.set_window_size(1920, 1080)

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']" )
user_name.send_keys('standart_use')
print("Input Login")

# С помощью этого метода нашли поле для ввода пароля и ввели неверный пароль
password = driver.find_element(By.XPATH, "//input[@id='password']" )
password.send_keys('secret_sauce')
print("Input Password")

bnt_login = driver.find_element(By.XPATH, "//input[@id='login-button']" )
bnt_login.click()
print("Click login button")

# Установил таймер задержки
time.sleep(5)
driver.refresh()