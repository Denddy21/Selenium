import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
# Сделалил кастомное правило которе не закрывает браузер автоматически после завершения скрипта
options.add_experimental_option("detach", True)
# Режим Headless в котором браузер не открывается
options.add_argument("--headless")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

try:
    base_url = 'https://www.saucedemo.com/'
    driver.get(base_url)
    driver.maximize_window()

    # Находим на странице поле для ввода имени
    user_name = driver.find_element(By.ID, 'user-name')
    user_name.send_keys('standard_user')  # Ввод имени в поле "usesname"
    print("Username passed")
    # С помощью другого типа XPATH (*) означает что тут мы ищем по всей странице Id = 'password'
    password = driver.find_element(By.ID, 'password')
    password.send_keys('secret_sauce')  # Ввод пароля в поле "password"
    print("Password passed")
    # Добавим переменную для поиска нужной кнопки на странице
    button_login = driver.find_element(By.ID, 'login-button')
    button_login.click()
    print("Login button pressed")

    current_url = driver.current_url
    print(driver.current_url)
    url_get = 'https://www.saucedemo.com/inventory.html'
    assert current_url == url_get
    print("Url cовпало")

    page_check = driver.find_element(By.XPATH, "//span[@class='title']")
    print(page_check.text)
    page_check = page_check.text
    assert page_check == 'Products'
    print("Находимся на нужной странице")

except Exception as e:
    # Этот блок сработает только при ошибке
    print("Тест упал с ошибкой", {e})

finally:
    driver.quit()
