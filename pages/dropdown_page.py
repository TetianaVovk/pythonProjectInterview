from playwright.sync_api import Page


class DropdownPage:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = f"{base_url}/dropdown"

        self.dropdown = page.locator("#dropdown")

    def open(self):
        self.page.goto(self.url)

    def select_option(self, value):
        self.dropdown.select_option(value)

    def get_selected_value(self):
        return self.dropdown.input_value()