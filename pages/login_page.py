from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = f"{base_url}/login"

        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")

    def open(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_flash_message(self):
        return self.flash_message
