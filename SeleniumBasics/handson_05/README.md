# Hands-On 05: Locators — ID, Name, XPath, CSS & Explicit Waits

This folder contains scripts demonstrating the use of locator strategies, XPath construction, dynamic waits handling, and form element interactions.

## Topics Covered
*   Locator strategies (ID, Name, Class Name, Tag Name, CSS Selector, XPath)
*   Creating robust relative XPath expressions
*   Expected Conditions and Explicit Waits (`WebDriverWait`)
*   Visibility vs. Clickability status handling

## Folder Structure
```text
handson_05/
├── checkbox_demo.py     # Checkbox selection and waits handling script
├── locator_demo.py      # CSS selectors & relative XPaths script
└── README.md
```

## How to Run
1. Install dependencies:
   ```bash
   pip install selenium webdriver-manager
   ```
2. Run the checkbox demo script:
   ```bash
   python checkbox_demo.py
   ```
3. Run the locator demo script:
   ```bash
   python locator_demo.py
   ```
