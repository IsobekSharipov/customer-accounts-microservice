"""Flask application for customer account management."""

from flask import Flask, jsonify, request

from service import configure_security


def create_app():
    """Create the customer accounts application."""
    app = Flask(__name__)
    configure_security(app)
    accounts = {}
    next_id = 1

    @app.get("/")
    def index():
        """Return service identity and status."""
        return jsonify(service="Customer Accounts Microservice", status="ok")

    @app.get("/health")
    def health():
        """Return a simple readiness indicator."""
        return jsonify(status="healthy"), 200

    @app.post("/accounts")
    def create_account():
        """Create a customer account."""
        nonlocal next_id
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify(error="A JSON object is required"), 400
        name = data.get("name")
        email = data.get("email")
        if not isinstance(name, str) or not name.strip():
            return jsonify(error="A nonempty name is required"), 400
        if not isinstance(email, str) or "@" not in email:
            return jsonify(error="A valid email is required"), 400
        account = {"id": next_id, "name": name.strip(), "email": email.strip()}
        accounts[next_id] = account
        next_id += 1
        return jsonify(account), 201

    @app.get("/accounts")
    def list_accounts():
        """List all customer accounts."""
        return jsonify(list(accounts.values())), 200

    @app.get("/accounts/<int:account_id>")
    def get_account(account_id):
        """Retrieve one customer account."""
        account = accounts.get(account_id)
        if account is None:
            return jsonify(error="Account not found"), 404
        return jsonify(account), 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
