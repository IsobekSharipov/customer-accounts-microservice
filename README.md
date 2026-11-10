# DevOps Capstone

## Customer Accounts Microservice

[![CI Build](https://github.com/IsobekSharipov/customer-accounts-microservice/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/IsobekSharipov/customer-accounts-microservice/actions/workflows/ci.yml)

**Project name:** DevOps Capstone — Customer Accounts Microservice

This DevOps Capstone project implements a Python/Flask customer accounts REST microservice and demonstrates Agile planning, continuous integration, security controls, Docker containerization, Kubernetes deployment, and Tekton CI/CD pipelines.

## Continuous Integration

The **CI** GitHub Actions workflow runs on pushes and pull requests targeting `main`. It checks out the source, installs dependencies, compiles Python files, and runs automated unit tests. The badge above reports the workflow's actual status; it cannot be manually set to passing.

- [CI workflow](.github/workflows/ci.yml)
- [CI Build workflow](.github/workflows/ci-build.yaml)
- [GitHub Actions runs](https://github.com/IsobekSharipov/customer-accounts-microservice/actions)

## Application endpoints

- `GET /` — service identity and status
- `GET /health` — health check
- `POST /accounts` — create a customer account
- `GET /accounts` — list customer accounts
- `GET /accounts/<id>` — read a customer account

## Project files

- `service/app.py` — Flask application
- `service/__init__.py` — security headers and CORS policies
- `tests/test_app.py` — automated tests
- `requirements.txt` — dependencies
- `Dockerfile` — Docker image definition
- `compose.yaml` — local container deployment
- `k8s/` — Kubernetes deployment and service
- `tekton/` — Tekton CI/CD pipelines

## Run locally

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m service.app
```

The application listens on port `8080`.
