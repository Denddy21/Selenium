import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
#Инициализация драйвера Firefox с автоматической установкой исполняемого файла GeckoDriver
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

time.sleep(10) #таймер работы сайта
driver.quit()
