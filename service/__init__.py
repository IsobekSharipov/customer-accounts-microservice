"""Customer Accounts microservice security configuration."""

from flask_talisman import Talisman


def configure_security(app):
    """Apply Talisman security headers to the Flask application."""
    Talisman(
        app,
        force_https=False,
        content_security_policy={"default-src": "'self'"},
        strict_transport_security=False,
        session_cookie_secure=False,
    )
