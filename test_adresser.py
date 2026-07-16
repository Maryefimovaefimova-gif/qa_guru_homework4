import time

from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://qa-guru.github.io/one-page-form/text-box.html"


def test_for_all_fields():
    print("Рефакторинг ")

    driver = webdriver.Chrome()

    try:
        
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(3)

        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Kylian Mbappe")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("kylian@guru.com")

        current_address_field = driver.find_element(By.ID, "currentAddress")
        current_address_field.send_keys("Москва; улица Цюрупы, дом 15, корп.3 квартира 168")

        permanent_address_field = driver.find_element(By.ID, "permanentAddress")
        permanent_address_field.send_keys("Калининград; улица Советская, дом 1, квартира 1")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(3) 

        result_box = driver.find_element(By.ID, "output")

        assert "Калининград; улица Советская, дом 1, квартира 1" in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()
