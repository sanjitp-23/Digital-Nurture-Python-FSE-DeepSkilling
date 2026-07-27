# Hands-On 09: Web Accessibility (a11y) & Cross-Browser Compatibility

This folder contains the implementation for Hands-On 09, auditing the Student Portal against WCAG 2.1 Web Accessibility guidelines and fixing semantic, ARIA, keyboard navigation, and color contrast issues.

## Topics Covered
*   Accessibility auditing (Lighthouse, axe DevTools)
*   Semantic HTML adjustments and Form label integrations
*   ARIA attributes (`aria-label`, `aria-current`, `aria-live`, `aria-expanded`)
*   Keyboard navigation control bindings (`tabindex`, keydown event listener)
*   WCAG 2.1 color contrast ratios validation

## Folder Structure
```text
handson_09/
├── index.html     # HTML page with accessibility fixes & ARIA annotations
├── app.js         # JavaScript file with keyboard support bindings
├── data.js        # Dataset file
├── styles.css     # CSS file with contrast fixes & focus style indicators
└── README.md
```

## How to Run
1. Open [index.html](file:///c:/Users/sanji/Sanjit%20P/Python_Backend_Frameworks_Solutions/Module%202%20-%20FrontendDev%20Solutions/handson_09/index.html) in your browser.
2. Test keyboard navigation using the `Tab` and `Enter` keys on course cards.
3. Perform accessibility audit using Chrome DevTools Lighthouse audit.
