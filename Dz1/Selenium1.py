from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# Оставляем браузер открытым после завершения скрипта
options.add_experimental_option("detach", True)
# Инициализация драйвера с автоматической установкой нужной версии
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
# Устанавливаем размер окна (Full HD)
driver.set_window_size(1920, 1080)
