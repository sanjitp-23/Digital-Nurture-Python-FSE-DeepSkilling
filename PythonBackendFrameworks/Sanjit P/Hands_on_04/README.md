# Hands-On 04: Flask — App Structure, Routing & Blueprints

This folder contains the implementation for Hands-On 04, building a structured Flask application using the Application Factory Pattern and modular Blueprints.

## Topics Covered
*   Flask Application Factory Pattern
*   Flask Configuration Classes
*   Modular Blueprints Design
*   Request Parsing and JSON Responses
*   Error Handlers Customization (404, 500)

## Folder Structure

```text
Hands_on_04/
└── flask_coursemanager/
    ├── courses/
    │   ├── routes.py      # Blueprint routes handler
    │   └── __init__.py
    ├── app.py             # Entry point (Application Factory create_app)
    └── config.py          # Configuration settings class
```

## How to Run

1.  Navigate to the project directory:
    ```bash
    cd "Python Backend Framework Solutions/Sanjit P/Hands_on_04/flask_coursemanager"
    ```
2.  Install Flask:
    ```bash
    pip install flask
    ```
3.  Run the Flask app:
    ```bash
    python app.py
    ```
4.  Test the REST API endpoints using Postman or cURL:
    *   `GET http://127.0.0.1:5000/api/courses`
