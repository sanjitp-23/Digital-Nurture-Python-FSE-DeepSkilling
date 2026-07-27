# Hands-On 07: FastAPI — Dependency Injection, CRUD & OpenAPI Documentation

This folder contains the implementation for Hands-On 07, expanding the FastAPI application to cover complete CRUD, Dependency Injection system, Background Tasks execution, and Swagger UI customizations.

## Topics Covered
*   FastAPI Dependency Injection (`Depends()`)
*   Response Models & Custom Status Codes
*   Background Tasks (e.g., email confirmation simulation)
*   OpenAPI Custom Metadata & endpoint tags

## Folder Structure

```text
Hands_on_07/
└── course_management/
    ├── database.py        # Async database engine
    ├── main.py            # CRUD routes, custom metadata & BackgroundTasks
    ├── models.py          # Relational models (SQLAlchemy)
    ├── schemas.py         # Request/Response validation (Pydantic)
    └── requirements.txt   # Dependencies file
```

## How to Run

1.  Navigate to the directory:
    ```bash
    cd "Python Backend Framework Solutions/Sanjit P/Hands_on_07/course_management"
    ```
2.  Install dependencies:
    ```bash
    pip install fastapi uvicorn sqlalchemy aiosqlite pydantic
    ```
3.  Run the application:
    ```bash
    uvicorn main:app --reload
    ```
4.  Open the API docs to test background tasks:
    *   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
