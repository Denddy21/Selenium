import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def start_test(browser_name: str) -> None:
    driver: webdriver.Remote

    if browser_name == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        print(f"Ошибка: браузер {browser_name} не найден. Используйте: chrome, firefox или edge")
        return

    # Логика теста
    driver.get('https://saucedemo.com')
    driver.maximize_window()
    time.sleep(3)
    driver.quit()


if __name__ == "__main__":
    # Проверяем, передал ли пользователь название браузера в терминале
    if len(sys.argv) > 1:
        chosen_browser = sys.argv[1].lower()
        start_test(chosen_browser)
    else:
        print("Пожалуйста, укажите браузер. Пример: python main.py chrome")
