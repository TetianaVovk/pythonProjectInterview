import pytest
from playwright.sync_api import expect, Page


@pytest.mark.smoke
def test_homepage_title(page: Page, base_url: str):
    page.goto(base_url)
    expect(page).to_have_title("The Internet")
