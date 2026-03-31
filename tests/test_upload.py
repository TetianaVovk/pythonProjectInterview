import pytest
from playwright.sync_api import expect
from pages.upload_page import UploadPage
from pathlib import Path


@pytest.mark.regression
def test_file_upload(page, base_url):

    upload = UploadPage(page, base_url)
    upload.open()

    file_path = Path("tests/test_file.txt")
    file_path.write_text("automation test file")

    upload.upload_file(str(file_path))

    expect(upload.uploaded_file).to_have_text("test_file.txt")