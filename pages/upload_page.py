from playwright.sync_api import Page


class UploadPage:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = f"{base_url}/upload"

        self.file_input = page.locator("#file-upload")
        self.submit_button = page.locator("#file-submit")
        self.uploaded_file = page.locator("#uploaded-files")

    def open(self):
        self.page.goto(self.url)

    def upload_file(self, file_path: str):
        self.file_input.set_input_files(file_path)
        self.submit_button.click()

    def get_uploaded_filename(self):
        return self.uploaded_file.inner_text()


