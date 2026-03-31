import requests


class UsersApi:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def get_user(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}", headers=self.headers)

    def create_user(self, payload):
        return requests.post(f"{self.base_url}/users", json=payload, headers=self.headers)

    def update_user(self, user_id, payload):
        return requests.put(f"{self.base_url}/users/{user_id}", json=payload, headers=self.headers)

    def delete_user(self, user_id):
        return requests.delete(f"{self.base_url}/users/{user_id}", headers=self.headers)