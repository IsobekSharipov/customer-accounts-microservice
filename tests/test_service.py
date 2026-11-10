"""Customer account REST service tests."""

import unittest

from service.app import create_app


class TestAccountService(unittest.TestCase):
    """Exercise create, list, read, update and delete account routes."""

    def setUp(self):
        self.client = create_app().test_client()

    def test_create_account(self):
        response = self.client.post(
            "/accounts", json={"name": "Ada", "email": "ada@example.com"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["id"], 1)

    def test_list_accounts(self):
        self.client.post(
            "/accounts", json={"name": "Ada", "email": "ada@example.com"}
        )
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_read_account(self):
        self.client.post(
            "/accounts", json={"name": "Ada", "email": "ada@example.com"}
        )
        response = self.client.get("/accounts/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "Ada")

    def test_update_account(self):
        self.client.post(
            "/accounts", json={"name": "Ada", "email": "ada@example.com"}
        )
        response = self.client.put(
            "/accounts/1", json={"name": "Updated", "email": "new@example.com"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "Updated")

    def test_delete_account(self):
        self.client.post(
            "/accounts", json={"name": "Ada", "email": "ada@example.com"}
        )
        response = self.client.delete("/accounts/1")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.client.get("/accounts/1").status_code, 404)

    def test_read_missing_account(self):
        self.assertEqual(self.client.get("/accounts/99").status_code, 404)

    def test_create_invalid_account(self):
        response = self.client.post("/accounts", json={"name": "", "email": "bad"})
        self.assertEqual(response.status_code, 400)

    def test_cors_preflight(self):
        response = self.client.options(
            "/accounts",
            headers={
                "Origin": "http://localhost:3000",
                "Access-Control-Request-Method": "POST",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.headers.get("Access-Control-Allow-Origin"),
            "http://localhost:3000",
        )


if __name__ == "__main__":
    unittest.main()
