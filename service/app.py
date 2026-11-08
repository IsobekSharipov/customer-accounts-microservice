"""Flask application for customer account management."""

from flask import Flask, jsonify


def create_app():
    """Create the customer accounts application."""
    app = Flask(__name__)

    @app.get("/")
    def index():
        """Return service identity and status."""
        return jsonify(service="Customer Accounts Microservice", status="ok")

    @app.get("/health")
    def health():
        """Return a simple readiness indicator."""
        return jsonify(status="healthy"), 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
