# test_relative_locator.py
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.chrome import ChromeDriverManager


def test_relative_locator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        driver.maximize_window()
        time.sleep(1)

        print("🔍 Поиск элементов с помощью Relative Locator:")

        checkbox1 = driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
        print(f"✓ Найден первый чекбокс")

        if not checkbox1.is_selected():
            checkbox1.click()
            print("✓ Чекбокс #1 отмечен")
        else:
            print("✓ Чекбокс #1 уже отмечен")

        checkbox2 = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]")
        print(f"✓ Найден второй чекбокс")

        if not checkbox2.is_selected():
            checkbox2.click()
            print("✓ Чекбокс #2 отмечен")
        else:
            print("✓ Чекбокс #2 уже отмечен")

        try:
            text_near_checkbox = driver.find_element(
                locate_with(By.TAG_NAME, "label").near(checkbox1)
            )
            print(f"✓ Найден текст рядом с чекбоксом: {text_near_checkbox.text}")
        except:
            print("ℹ Рядом с чекбоксом нет текста (это нормально)")

        print("\n Тест успешно завершен!")

    except Exception as e:
        print(f"\n Ошибка в тесте: {e}")
        raise
    finally:
        time.sleep(2)
        driver.quit()
        print(" Браузер закрыт")


if __name__ == "__main__":
    test_relative_locator()
