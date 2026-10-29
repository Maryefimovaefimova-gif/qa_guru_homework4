import pytest
from conftest import DESKTOP_PARAMS, MOBILE_PARAMS
from page_github import GitHubPage


@pytest.mark.parametrize("desktop_driver", DESKTOP_PARAMS, indirect=True)
def test_desktop_sign_in_param_skip(desktop_driver):
    page = GitHubPage(desktop_driver)

    page.open()
    page.click_desktop_sign_in()

    assert "login" in page.get_current_url()


@pytest.mark.parametrize("mobile_driver", MOBILE_PARAMS, indirect=True)
def test_mobile_sign_in_param_skip(mobile_driver):
    page = GitHubPage(mobile_driver)

    page.open()
    page.click_mobile_sign_in()

    assert "login" in page.get_current_url()