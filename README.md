# Functional Testing Project

![Functional Testing CI](https://github.com/Sazzadhstucse/functional-testing-2608110/actions/workflows/ci.yml/badge.svg)

## Project Overview

This project is developed as part of a practical assignment on Functional Testing, CI/CD, and Live Deployment.

The project tests 16 functions from the original `target.py` module using pytest. It covers valid inputs, boundary cases, invalid inputs, exception handling, and mathematical operations.

A Flask-based web application is also included, allowing users to execute the functions and view their results or error messages through a browser.

The original `target.py` file is kept unchanged.

## Live Application

**Live URL:** https://functional-testing-2608110.onrender.com

**Health Check:** https://functional-testing-2608110.onrender.com/health

The health endpoint returns the application status and deployed Git commit SHA.

## Technologies Used

- Python
- pytest
- pytest-cov
- Ruff
- Flask
- Gunicorn
- Git and GitHub
- GitHub Actions
- Render

## Project Structure

```text
functional-testing/
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   ├── test_target.py
│   └── test_app.py
├── app.py
├── target.py
├── requirements.txt
├── .gitignore
├── Procfile
├── render.yaml
└── README.md
```

## Installation

Install Python 3.10 or later.

Clone the repository:

```bash
git clone https://github.com/Sazzadhstucse/functional-testing-2608110.git
cd functional-testing-2608110
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run Tests

Run the complete test suite:

```bash
python -m pytest
```

Run tests with line and branch coverage:

```bash
python -m pytest --cov=target --cov-branch --cov-fail-under=100 --cov-report=term-missing --cov-report=xml
```

Run code linting:

```bash
python -m ruff check .
```

## Test Coverage

The test suite covers all 16 functions in `target.py`.

**Achieved Coverage:**

- Statement Coverage: 100%
- Branch Coverage: 100%
- Total Test Cases: 125 (including Flask application tests)

GitHub Actions runs the test suite using Python 3.10, 3.11, and 3.12.

## Continuous Integration and Deployment

GitHub Actions is configured to run automatically on:

- Pushes to the `main` branch.
- Pull requests targeting the `main` branch.

The CI/CD pipeline performs the following steps:

1. Checks out the repository.
2. Sets up Python 3.10, 3.11, and 3.12.
3. Installs project dependencies.
4. Runs Ruff linting.
5. Executes pytest with 100% line and branch coverage requirements.
6. Uploads coverage reports as GitHub Actions artifacts.
7. Triggers Render deployment after successful tests on pushes to `main`.
8. Performs live smoke tests after deployment.
9. Verifies that the deployed commit SHA matches the GitHub commit SHA.

Deployment is blocked if the test job fails.

## Web Application

The Flask web application provides a browser-based interface to execute functions from `target.py`.

Features include:

- Function selection.
- JSON-based argument input.
- Function execution.
- Display of returned results.
- Display of exception types and error messages.
- Health-check endpoint with deployment commit information.

## Live Deployment

The application is deployed on Render using Gunicorn.

**Application URL:** https://functional-testing-2608110.onrender.com

**Health Endpoint:** https://functional-testing-2608110.onrender.com/health

Render deployment is triggered through GitHub Actions after successful CI testing.

Note: The free Render instance may spin down after inactivity, causing a delay on the first request.

## Suspected Bugs and Potential Edge Cases

The original `target.py` is intentionally preserved without modification.

Testing and code review identified potential input-validation limitations:

- `greet()` may raise an unexpected `AttributeError` when a non-string value other than `None` is provided.
- `find_max()` and `average()` require inputs that support `len()` and iteration.
- `common_items()` expects compatible set-like inputs.
- `get_price()` expects a mapping-like object containing the requested key.

These behaviors are documented as potential limitations rather than changes to the original implementation.

## Author

**Student ID:** 2608110

**GitHub Repository:** https://github.com/Sazzadhstucse/functional-testing-2608110
