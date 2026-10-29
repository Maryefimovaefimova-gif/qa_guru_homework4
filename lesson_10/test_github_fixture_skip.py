import pytest
from conftest import ALL_SIZES
from page_github import GitHubPage

SIZE_IDS = ["Wisecoco", "Acer", "LG", "iPhone 16 Pro", "Samsung Galaxy S25", "Xiaomi"]


@pytest.mark.parametrize("desktop_driver", ALL_SIZES, indirect=True, ids=SIZE_IDS)
def test_desktop_sign_in_with_skip(desktop_driver):
    page = GitHubPage(desktop_driver)

    page.open()
    page.click_desktop_sign_in()

    assert "login" in page.get_current_url()


@pytest.mark.parametrize("mobile_driver", ALL_SIZES, indirect=True, ids=SIZE_IDS)
def test_mobile_sign_in_with_skip(mobile_driver):
    page = GitHubPage(mobile_driver)

    page.open()
    page.click_mobile_sign_in()

    assert "login" in page.get_current_url()