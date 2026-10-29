import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


class GitHubPage:
    URL = "https://github.com"

    DESKTOP_SIGN_IN = (By.CSS_SELECTOR, "a[data-analytics-event*='sign_in'][class*='desktopAction']")
    MOBILE_SIGN_IN = (By.CSS_SELECTOR, "a[data-analytics-event*='sign_in']:not([class*='signInDesktop'])")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.driver.get(self.URL)

    def click_desktop_sign_in(self):
        element = self.wait.until(ec.element_to_be_clickable(self.DESKTOP_SIGN_IN))
        element.click()

    def click_mobile_sign_in(self):
        element = self.wait.until(ec.element_to_be_clickable(self.MOBILE_SIGN_IN))
        element.click()

    def get_current_url(self):
        return self.driver.current_url

@pytest.fixture
def desktop_driver(request):
    options = Options()
    driver = webdriver.Chrome(options=options)
    width, height = request.param
    driver.set_window_size(width, height)
    yield driver
    driver.quit()


@pytest.fixture
def mobile_driver(request):
    options = Options()
    driver = webdriver.Chrome(options=options)
    width, height = request.param
    driver.set_window_size(width, height)
    yield driver
    driver.quit()
