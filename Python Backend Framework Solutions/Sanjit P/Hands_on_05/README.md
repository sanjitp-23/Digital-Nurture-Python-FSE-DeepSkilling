# Hands-On 05: Flask with SQLAlchemy ORM & Database Integration

This folder contains the implementation for Hands-On 05, integrating Flask with SQLAlchemy ORM, defining relationships, running database migrations, and connecting ORM queries to REST endpoints.

## Topics Covered
*   Flask-SQLAlchemy Integration
*   Database Schema Migrations via Flask-Migrate (Alembic)
*   SQLAlchemy ORM Relationships
*   Connecting database queries to API routes

## Folder Structure

```text
Hands_on_05/
└── flask_coursemanager/
    ├── courses/
    │   ├── models.py      # Department, Course, Student, Enrollment models
    │   ├── routes.py      # Routes with SQLAlchemy queries & JOINs
    │   └── __init__.py
    ├── migrations/        # Alembic database migrations history
    ├── app.py             # App instantiation & config mapping
    ├── config.py          # Database URI & configuration settings
    └── extensions.py      # Extensible db, migrate declarations
```

## How to Run

1.  Navigate to the project directory:
    ```bash
    cd "Python Backend Framework Solutions/Sanjit P/Hands_on_05/flask_coursemanager"
    ```
2.  Install requirements:
    ```bash
    pip install flask flask-sqlalchemy flask-migrate
    ```
3.  Perform migrations:
    ```bash
    flask db init
    flask db migrate -m "initial schema"
    flask db upgrade
    ```
4.  Run the Flask app:
    ```bash
    python app.py
    ```
