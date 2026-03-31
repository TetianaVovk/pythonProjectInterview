import pytest
from playwright.sync_api import expect
from pages.dropdown_page import DropdownPage


@pytest.mark.regression
def test_select_option(page, base_url):

    dropdown = DropdownPage(page, base_url)
    dropdown.open()

    dropdown.select_option("1")

    expect(dropdown.dropdown).to_have_value("1")