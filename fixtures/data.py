import pytest

INVALID_LOGIN_CASES = [
    pytest.param(
        {
            "username": "tomsmith",
            "password": "wrong",
            "expected": "Your password is invalid!",
        },
        id="wrong_password",
    ),
    pytest.param(
        {
            "username": "wrong",
            "password": "SuperSecretPassword!",
            "expected": "Your username is invalid!",
        },
        id="wrong_username",
    ),
]

VALID_USER = {
    "username": "tomsmith",
    "password": "SuperSecretPassword!",
    "expected": "You logged into a secure area!"
}
