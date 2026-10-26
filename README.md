# Functional Testing Project

## Project Overview
This project tests 16 functions from `target.py` using pytest. It covers valid inputs, boundary cases, invalid inputs, exception handling, and mathematical operations.

## Technologies Used
- Python
- pytest
- pytest-cov
- Git and GitHub
- GitHub Actions

## Project Structure

```text
functional-testing/
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_target.py
├── target.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Install Python 3.10 or later, then install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run Tests

Run the complete test suite with branch coverage:

```bash
python -m pytest --cov=target --cov-branch --cov-fail-under=100 --cov-report=term-missing --cov-report=xml
```

## Test Coverage

The local test suite has achieved 100% statement and branch coverage in the tested environment. GitHub Actions runs the tests using Python 3.10, 3.11, and 3.12.

## Continuous Integration

GitHub Actions automatically runs tests when code is pushed to the `main` branch or when a pull request targets `main`.

## Live Deployment

Live deployment URL: Not deployed yet.

## Suspected Bugs

Potential edge cases and unexpected behaviors discovered during testing should be documented here. The original `target.py` is kept unchanged.

## Author

Student ID: 2608110