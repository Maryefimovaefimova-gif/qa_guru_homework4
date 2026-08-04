import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_drag_and_drop(driver):
    driver.get("https://demoqa.com/droppable")
    time.sleep(3)

    all_elements = driver.find_elements(By.XPATH, "//*[@id]")
    for elem in all_elements:
        print(f"ID: {elem.get_attribute('id')}, Tag: {elem.tag_name}")

    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    action = ActionChains(driver)
    action.drag_and_drop(source, target).perform()
