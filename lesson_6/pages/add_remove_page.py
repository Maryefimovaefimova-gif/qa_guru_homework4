from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AddRemovePage:
    ADD_BUTTON = (By.XPATH, "//button[text()='Add Element']")
    DELETE_BUTTON = (By.XPATH, "//button[text()='Delete']")
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.presence_of_element_located(self.ADD_BUTTON))
        return self

    def add_element(self):
        button = self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON))
        button.click()
        return self

    def get_delete_buttons(self):
        return self.driver.find_elements(*self.DELETE_BUTTON)

    def delete_all(self):
        while self.get_delete_buttons():
            buttons = self.get_delete_buttons()
            if buttons:
                buttons[0].click()
        return self
