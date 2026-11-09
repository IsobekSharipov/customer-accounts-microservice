"""HTTP endpoint and security configuration tests."""

import unittest

from service.app import create_app


class CustomerAccountsAppTests(unittest.TestCase):
    """Validate the application startup and security headers."""

    def setUp(self):
        """Create an isolated Flask test client."""
        self.client = create_app().test_client()

    def test_index(self):
        """The root endpoint identifies the microservice."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["service"], "Customer Accounts Microservice"
        )

    def test_health(self):
        """The health endpoint returns HTTP 200."""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "healthy")

    def test_security_headers(self):
        """Talisman supplies common response security headers."""
        response = self.client.get("/health")
        self.assertIn("Content-Security-Policy", response.headers)
        self.assertEqual(response.headers.get("X-Content-Type-Options"), "nosniff")
        self.assertEqual(response.headers.get("X-Frame-Options"), "SAMEORIGIN")

    def test_cors_allowed_origin(self):
        """An approved origin may access the accounts endpoint."""
        response = self.client.get(
            "/accounts", headers={"Origin": "http://localhost:3000"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.headers.get("Access-Control-Allow-Origin"),
            "http://localhost:3000",
        )

    def test_cors_disallowed_origin(self):
        """An unapproved origin does not receive CORS permission."""
        response = self.client.get(
            "/accounts", headers={"Origin": "https://untrusted.example"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("Access-Control-Allow-Origin", response.headers)


if __name__ == "__main__":
    unittest.main()
