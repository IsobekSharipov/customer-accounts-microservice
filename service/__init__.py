"""Customer Accounts microservice security configuration."""

from flask_cors import CORS
from flask_talisman import Talisman


def configure_security(app):
    """Apply Talisman security headers and restricted CORS policies."""
    Talisman(
        app,
        force_https=False,
        content_security_policy={"default-src": "'self'"},
        strict_transport_security=False,
        session_cookie_secure=False,
    )
    CORS(
        app,
        resources={r"/accounts*": {"origins": ["http://localhost:3000"]}},
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Content-Type"],
    )
