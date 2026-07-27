# Hands-On 01: Web Framework Foundations & Django Project Setup

This folder contains the implementation for Hands-On 01, introducing basic web framework architecture and setting up a Django project.

## Topics Covered
*   Web Framework Concepts
*   Request-Response Cycle
*   Django Project Setup
*   MVC / MVT Pattern
*   WSGI vs. ASGI
*   URL Routing & Middleware

## Folder Structure

```text
Hands_on_01/
├── courses/               # Main Django application module
│   ├── asgi.py            # ASGI config for async servers
│   ├── settings.py        # Django project configuration settings
│   ├── urls.py            # URL routing configurations
│   ├── wsgi.py            # WSGI config for sync web servers
│   └── __init__.py
├── Sample/                # App containing views and templates
│   ├── admin.py           # Admin interface registration
│   ├── apps.py            # App configurations
│   ├── models.py          # Data models
│   ├── tests.py           # Test suites
│   ├── urls.py            # App-level routing
│   └── views.py           # Views (e.g., hello_view)
└── manage.py              # Django project command-line utility
```

## How to Run

1.  Navigate to the project root directory:
    ```bash
    cd "Python Backend Framework Solutions/Sanjit P/Hands_on_01"
    ```
2.  Install Django:
    ```bash
    pip install django
    ```
3.  Start the development server:
    ```bash
    python manage.py runserver
    ```
4.  Verify in your browser or client at:
    *   [http://127.0.0.1:8000/api/hello/](http://127.0.0.1:8000/api/hello/)
