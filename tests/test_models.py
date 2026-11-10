"""Account model unit tests."""

import unittest

from service.models import Account


class TestAccountModel(unittest.TestCase):
    """Verify account data and serialization."""

    def test_account_fields(self):
        account = Account(1, "Ada", "ada@example.com")
        self.assertEqual(account.id, 1)
        self.assertEqual(account.name, "Ada")
        self.assertEqual(account.email, "ada@example.com")

    def test_account_to_dict(self):
        account = Account(2, "Grace", "grace@example.com")
        self.assertEqual(
            account.to_dict(),
            {"id": 2, "name": "Grace", "email": "grace@example.com"},
        )


if __name__ == "__main__":
    unittest.main()
