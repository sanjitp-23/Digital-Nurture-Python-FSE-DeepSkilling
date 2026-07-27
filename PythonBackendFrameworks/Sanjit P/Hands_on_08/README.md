# Hands-On 08: RESTful API Design Best Practices

This folder contains the implementation for Hands-On 08, refactoring existing APIs to follow strict REST principles, custom pagination strategies, API versioning, and standardized error formats.

## Topics Covered
*   REST resource naming conventions (plural nouns)
*   Location response header for POST endpoints
*   URL versioning (`/api/v1/`)
*   Offset pagination system
*   Standardized error response payloads format

## Folder Structure

```text
Hands_on_08/
└── course_management/
    ├── database.py        # Async session configuration
    ├── main.py            # API with versioning, pagination, search, standardized errors
    ├── models.py          # SQLAlchemy models
    ├── schemas.py         # Versioned Pydantic schemas
    └── requirements.txt
```

## How to Run

1.  Navigate to the directory:
    ```bash
    cd "Python Backend Framework Solutions/Sanjit P/Hands_on_08/course_management"
    ```
2.  Install dependencies:
    ```bash
    pip install fastapi uvicorn sqlalchemy aiosqlite pydantic
    ```
3.  Start server:
    ```bash
    uvicorn main:app --reload
    ```
4.  Test endpoints in docs UI:
    *   Versioning: [http://127.0.0.1:8000/api/v1/courses/](http://127.0.0.1:8000/api/v1/courses/)
    *   Pagination: `GET /api/v1/courses/?page=1&page_size=2`
    *   Standard Error structure when accessing unknown IDs.
