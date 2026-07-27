# Hands-On 04: Selenium WebDriver Setup & Basic Commands

This folder contains scripts implementing the initial Selenium WebDriver setup, navigating through pages, managing multiple browser windows/tabs, and taking screenshots.

## Topics Covered
*   WebDriver Architecture and setup using `webdriver-manager`
*   Implicit waits and basic window commands
*   Capturing screenshots on specific steps
*   Browser size controls (`set_window_size`)

## Folder Structure
```text
handson_04/
├── screenshots/
│   └── playground_screenshot.png # Captured screenshot file
├── navigation_test.py             # Navigation, tabs, and window resizing script
├── setup_test.py                  # WebDriver initialization script
└── README.md
```

## How to Run
1. Install Python dependencies:
   ```bash
   pip install selenium webdriver-manager
   ```
2. Run the setup script:
   ```bash
   python setup_test.py
   ```
3. Run the navigation test script:
   ```bash
   python navigation_test.py
   ```
