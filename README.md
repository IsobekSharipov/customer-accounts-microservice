# Customer Accounts Microservice

[![CI](https://github.com/IsobekSharipov/customer-accounts-microservice/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/IsobekSharipov/customer-accounts-microservice/actions/workflows/ci.yml)

**Project name:** Customer Accounts Microservice

A Python/Flask microservice project for the IBM capstone assignment. The goal is to develop customer account management REST APIs, practice agile planning, implement automated testing and security checks, and prepare Docker and Kubernetes deployment.

## Continuous Integration

The badge above reports the actual outcome of the GitHub Actions **CI** workflow on the `main` branch. It is not a manually assigned passing status.

Workflow: [`.github/workflows/ci.yml`](.github/workflows/ci.yml).

The initial workflow checks out the repository, installs Python dependencies, compiles source code, and runs unit tests.

## Initial application

- `GET /` — service identification and status
- `GET /health` — health check
- `service/app.py` — Flask application factory
- `tests/test_app.py` — automated unit tests
- `requirements.txt` — Python dependencies

## Run locally

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m service.app
```

The development service listens on port `8080`. Customer account APIs, security, Docker configuration and Kubernetes manifests will be developed in subsequent capstone tasks.
