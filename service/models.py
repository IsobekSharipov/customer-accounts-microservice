"""Account domain model for the customer accounts service."""

from dataclasses import dataclass


@dataclass
class Account:
    """A customer account with a unique identifier and contact details."""

    id: int
    name: str
    email: str

    def to_dict(self):
        """Return the JSON-compatible account representation."""
        return {"id": self.id, "name": self.name, "email": self.email}
