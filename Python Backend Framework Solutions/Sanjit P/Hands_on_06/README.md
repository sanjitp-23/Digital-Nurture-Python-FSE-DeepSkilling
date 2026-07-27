# Hands-On 06: FastAPI — Path Parameters, Pydantic & Async Endpoints

This folder contains the implementation for Hands-On 06, building a high-performance asynchronous API using FastAPI, request validation using Pydantic, and async SQLAlchemy queries.

## Topics Covered
*   FastAPI Async Endpoints
*   Pydantic Schemas request/response validation
*   Path & Query parameters
*   SQLAlchemy Async Engine with SQLite
*   Automated OpenAPI (Swagger UI) documentation

## Folder Structure

```text
Hands_on_06/
└── handson_6/
    ├── database.py        # Async engine & sessionmaker config
    ├── main.py            # API routing, dependecy inject, CRUD
    ├── models.py          # SQLAlchemy models definition
    ├── schemas.py         # Pydantic schemas validation
    ├── requirements.txt   # Packages requirements listing
    └── courses.db         # Local SQLite DB
```

## How to Run

1.  Navigate to the project directory:
    ```bash
    cd "Python Backend Framework Solutions/Sanjit P/Hands_on_06/handson_6"
    ```
2.  Install dependencies:
    ```bash
    pip install fastapi uvicorn sqlalchemy aiosqlite pydantic
    ```
3.  Start server using Uvicorn:
    ```bash
    uvicorn main:app --reload
    ```
4.  Open the Swagger UI documentation at:
    *   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
