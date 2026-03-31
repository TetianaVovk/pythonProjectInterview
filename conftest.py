import os
import re
from pathlib import Path
import pytest
from fixtures.data import INVALID_LOGIN_CASES, VALID_USER

ARTIFACTS_DIR = Path("artifacts/screenshots")


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://the-internet.herokuapp.com")


def _safe_name(nodeid: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_]+", "_", nodeid)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        item.rep_call = rep


@pytest.fixture(autouse=True)
def screenshot_on_failure(request):
    yield

    rep = getattr(request.node, "rep_call", None)

    if rep and rep.failed:
        if "page" in request.fixturenames:
            page = request.getfixturevalue("page")

            ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
            file_name = _safe_name(request.node.nodeid) + ".png"
            screenshot_path = ARTIFACTS_DIR / file_name

            page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"\n📸 Screenshot saved to: {screenshot_path}")


@pytest.fixture
def valid_user():
    return VALID_USER


@pytest.fixture(params=INVALID_LOGIN_CASES)
def invalid_login_data(request):
    return request.param
