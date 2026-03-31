import requests
from jsonschema import validate
from tests.schemas.user_schema import USER_SCHEMA


def test_get_user_schema(api_base_url, api_headers):
    response = requests.get(f"{api_base_url}/users/2", headers=api_headers)

    assert response.status_code == 200

    data = response.json()

    validate(instance=data, schema=USER_SCHEMA)
