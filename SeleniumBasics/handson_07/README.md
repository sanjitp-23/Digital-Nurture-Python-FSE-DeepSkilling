# Hands-On 07: Page Object Model (POM) Design Pattern

This folder contains exercises structuring automated web UI tests using the Page Object Model (POM) design pattern to achieve high test maintainability and code reusability.

## Topics Covered
*   Page Object Model (POM) design pattern principles
*   Encapsulating page locators and user actions within Page Classes
*   Separating testing assert logic from page interactions
*   Refactoring flat scripts into scalable object-oriented test suites

## Folder Structure
```text
handson_07/
├── pages/
│   ├── __init__.py
│   ├── base_page.py        # Common base page behaviors mapping
│   ├── checkbox_page.py    # Checkbox interactions page class
│   ├── dropdown_page.py    # Dropdown interactions page class
│   ├── input_form_page.py  # Input form fields page class
│   └── simple_form_page.py # Simple forms validation page class
├── tests/
│   ├── __init__.py
│   └── test_pom_playground.py # Pytest test cases using page classes
├── conftest.py             # Shared fixtures and screenshot-on-failure hooks
├── pytest.ini              # Pytest configuration settings
├── report.html             # Generated HTML execution report
└── README.md
```

## How to Run
1. Navigate to the project directory:
   ```bash
   cd "SeleniumBasics/handson_07"
   ```
2. Install package dependencies:
   ```bash
   pip install pytest pytest-html selenium webdriver-manager
   ```
3. Run the POM test suite and generate an HTML report:
   ```bash
   pytest tests/test_pom_playground.py -v --html=report.html --self-contained-html
   ```
