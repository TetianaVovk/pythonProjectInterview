import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_success(page, base_url, valid_user):
    login = LoginPage(page, base_url)
    login.open()
    login.login(valid_user["username"], valid_user["password"])

    expect(login.get_flash_message()).to_contain_text(valid_user["expected"])
