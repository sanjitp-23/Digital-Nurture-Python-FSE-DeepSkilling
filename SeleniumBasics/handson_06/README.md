# Hands-On 06: Running Selenium Tests with pytest — Fixtures & Reporting

This folder contains exercises implementing the Pytest framework to execute Selenium tests, configure reusable driver fixtures, parameterize input fields, and generate HTML execution reports.

## Topics Covered
*   Pytest basics and automatic test discovery
*   Creating shared setup/teardown hooks in `conftest.py`
*   Test parameterization (`@pytest.mark.parametrize`)
*   Capturing screenshots dynamically on test failures
*   Generating HTML test execution reports (`pytest-html`)

## Folder Structure
```text
handson_06/
├── conftest.py          # Pytest fixtures and screenshot-on-failure hooks
├── pytest.ini           # Pytest configurations
├── test_playground.py   # Test suite for forms & checkboxes
├── report.html          # Generated test execution HTML report
└── README.md
```

## How to Run
1. Install testing dependencies:
   ```bash
   pip install pytest pytest-html selenium webdriver-manager
   ```
2. Execute the test suite:
   ```bash
   pytest test_playground.py -v
   ```
3. Run tests and generate an HTML report:
   ```bash
   pytest test_playground.py -v --html=report.html --self-contained-html
   ```
