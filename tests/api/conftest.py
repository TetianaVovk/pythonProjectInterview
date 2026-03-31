import pytest
from utils.config import BASE_API_URL, REQRES_API_KEY


@pytest.fixture
def api_base_url():
    return BASE_API_URL


@pytest.fixture
def api_headers():
    return {
        "x-api-key": REQRES_API_KEY,
        "Content-Type": "application/json"
    }