import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage


@pytest.mark.regression
def test_login_negative(page, base_url, invalid_login_data):

    login = LoginPage(page, base_url)
    login.open()
    login.login(invalid_login_data["username"], invalid_login_data["password"])

    expect(login.get_flash_message()).to_contain_text(invalid_login_data["expected"])
