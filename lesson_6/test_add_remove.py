from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.add_remove_page import AddRemovePage


def test_add_remove_elements():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        page = AddRemovePage(driver)
        page.open()

        for i in range(3):
            page.add_element()
            print(f"Добавлен элемент {i + 1}")

        buttons = page.get_delete_buttons()
        assert len(buttons) == 3, f"Ожидалось 3 кнопки, найдено {len(buttons)}"
        print(f"Найдено {len(buttons)} кнопок Delete")

        page.delete_all()

        final_buttons = page.get_delete_buttons()
        assert len(final_buttons) == 0, f"Ожидалось 0 кнопок, найдено {len(final_buttons)}"

        print("Тест пройден!")

    except Exception as e:
        print(f" Ошибка: {e}")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    test_add_remove_elements()
