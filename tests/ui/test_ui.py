import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.mark.ui
def test_check_incorrect_username():
    # створення об'єкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(r"C:\\Users\\Елена\\lena_repo1" + r"\\chromedriver-win64")
    )

    # відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # закриваємо браузер
    driver.close
