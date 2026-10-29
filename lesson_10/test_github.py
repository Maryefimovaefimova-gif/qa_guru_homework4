import pytest
from page_github import GitHubPage
from constants import DESKTOP_SIZES, MOBILE_SIZES


@pytest.mark.parametrize("desktop_driver", DESKTOP_SIZES, indirect=True, ids=["Wisecoco", "Acer"])
def test_desktop_sign_in(desktop_driver):
    page = GitHubPage(desktop_driver)

    page.open()
    page.click_desktop_sign_in()

    assert "login" in page.get_current_url()


@pytest.mark.parametrize("mobile_driver", MOBILE_SIZES, indirect=True,
                         ids=["iPhone 16 Pro", "Samsung Galaxy S25"])
def test_mobile_sign_in(mobile_driver):
    page = GitHubPage(mobile_driver)

    page.open()
    page.click_mobile_sign_in()

    assert "login" in page.get_current_url()