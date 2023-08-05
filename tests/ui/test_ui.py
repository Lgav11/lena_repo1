import pytest

from selenium import webdriver

# тут замість chrome можна вказувати інший браузер
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_check_incorrect_username():
    # створення об'єкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(
            r"C:\\Users\\Елена\\lena_repo1\\chromedriver" + "\\chromedriver.exe"
        )
    )

    # відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # знаходимо поле в яке будемо додавати неправ. ім\імейл
    login_elem = driver.find_element(By.ID, "login_field")

    # вводимо неправ імейл
    login_elem.send_keys("dsdsds.gmail.com")

    # знаходимо поле паролю
    pass_elem = driver.find_element(By.ID, "password")

    # вводимо неправ пароль
    pass_elem.send_keys("wrong")

    # знаходимо кнопку
    btn_elem = driver.find_element(By.NAME, "commit")

    # емулюємо клік
    btn_elem.click()

    assert driver.title == "Sign in to GitHub · GitHub"
    time.sleep(2)  # додаємо затримку

    # закриваємо браузер
    driver.close
