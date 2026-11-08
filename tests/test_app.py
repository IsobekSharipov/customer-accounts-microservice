"""Basic HTTP endpoint tests."""

import unittest

from service.app import create_app


class CustomerAccountsAppTests(unittest.TestCase):
    """Validate the application startup and health endpoints."""

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


if __name__ == "__main__":
    unittest.main()
