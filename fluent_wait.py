import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


base_url="https://qa-guru.github.io/one-page-form/text-box.html"
def test_fluent_wait():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(base_url)

        time.sleep(5)

        driver.find_element(By.ID, "userName").send_keys("Иван Иванов")
        driver.find_element(By.ID, "userEmail").send_keys("ivan@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("ул. Ленина, дом 1")
        driver.find_element(By.ID, "permanentAddress").send_keys("ул. Пушкина, дом 10")

        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        fluent_wait = WebDriverWait(
            driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        )

        output_block = fluent_wait.until(EC.visibility_of_element_located((By.ID, "output")))

        time.sleep(5)

        print("Тест №1 успешно пройден! Блок с результатами появился.")
        assert output_block.is_displayed()

    finally:
        driver.quit()


def test_fluent_empty_wait():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(base_url)

        time.sleep(5)

        driver.find_element(By.ID, "userName").send_keys("")
        driver.find_element(By.ID, "userEmail").send_keys("")
        driver.find_element(By.ID, "currentAddress").send_keys("")
        driver.find_element(By.ID, "permanentAddress").send_keys("")


        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        fluent_wait = WebDriverWait(
            driver,
            timeout=0,
            poll_frequency=0,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        )

        output_block = fluent_wait.until(EC.visibility_of_element_located((By.ID, "output")))

        time.sleep(5)

        print("Тест №2 успешно пройден! Блок с пустыми результатами появился.")
        assert output_block.is_displayed()

    finally:

        driver.quit()


