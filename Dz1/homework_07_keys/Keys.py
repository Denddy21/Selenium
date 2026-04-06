from selenium.webdriver.common.keys import Keys
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
user_name.send_keys('standard_user')
print("Input Login")
time.sleep(2)
user_name.send_keys(Keys.COMMAND + 'a') #Имитировали нажатие cmd + a для выбора текста
time.sleep(1)
user_name.send_keys(Keys.DELETE) # Имитировали кнопку delete, чтобы удалить выделенное поле

#С помощью этого метода нашли поле для ввода пароля и ввели неверный пароль
password = driver.find_element(By.XPATH, "//input[@id='password']" )
password.send_keys("secret_sauce")
print("Input Password")
time.sleep(1)
password.send_keys(Keys.COMMAND + 'a')
time.sleep(1)
password.send_keys(Keys.DELETE)

bnt_login = driver.find_element(By.XPATH, "//input[@id='login-button']" )
bnt_login.click()
print("Click login button")
time.sleep(1)
driver.close()