import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = "https://qa-guru.github.io/one-page-form/text-box.html"


def test01():
    """Негативный тест: email содержит спецсимвол"""
    try:
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(3)

        invalid_emails = [
            "ivanov@ example.com"

        ]

        for invalid_email in invalid_emails:
            driver.refresh()
            time.sleep(3)

            driver.find_element(By.ID, "userName").send_keys("Иван Иванов")
            driver.find_element(By.ID, "userEmail").send_keys(invalid_email)

            driver.find_element(By.ID, "submit").click()
            time.sleep(3)

            result_field = driver.find_element(By.ID, "output")
            result_text = result_field.text

            assert invalid_email not in result_text, f"Ожидался корректный email: '{result_text}'"

        print("negative test01: passed")

    finally:
        driver.quit()
