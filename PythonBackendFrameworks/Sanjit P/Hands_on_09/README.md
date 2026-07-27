# Hands-On 09: Authentication & Security — JWT, OAuth2 & OWASP

This folder contains the implementation for Hands-On 09, securing the application with hashed passwords, JWT token authentication, route protection dependencies, CORS setups, and OWASP recommendations.

## Topics Covered
*   Bcrypt password hashing (using Passlib)
*   JWT access tokens creation (using python-jose)
*   FastAPI dependency route protection (`Depends(oauth2_scheme)`)
*   CORS configuration middleware
*   OWASP Top 10 awareness (hashing vs plaintext storage)

## Folder Structure

```text
Hands_on_09/
└── course_management/
    ├── security.py        # Bcrypt setup and password verification logic
    ├── main.py            # JWT token endpoints, dependencies, cors mapping
    ├── database.py
    ├── models.py
    ├── schemas.py
    └── requirements.txt
```

## How to Run

1.  Navigate to the directory:
    ```bash
    cd "Python Backend Framework Solutions/Sanjit P/Hands_on_09/course_management"
    ```
2.  Install dependencies:
    ```bash
    pip install fastapi uvicorn sqlalchemy aiosqlite pydantic passlib[bcrypt] python-jose[cryptography] python-multipart
    ```
3.  Start server:
    ```bash
    uvicorn main:app --reload
    ```
4.  Test endpoints:
    *   Register User: `POST /api/v1/auth/register/`
    *   Login & Get JWT: `POST /api/v1/auth/login/`
    *   Access protected endpoints (e.g. creating a course) by providing the `Authorization: Bearer <token>` header.
