# Hands-On 06: ORM Integration — SQLAlchemy Core & ORM

This folder contains SQLAlchemy implementation mapping the `college_db` relational database schemas, defining relationships, running session-based CRUD operations, and configuring Eager Loading to resolve N+1 queries.

## Topics Covered
*   SQLAlchemy models mapping & connection engine setups
*   Session transactions CRUD (add, commit, query, delete)
*   Bidirectional relationships mappings (`relationship()`)
*   Eager loading using `joinedload()` to optimize queries count

## Folder Structure

```text
hands_on_6/
├── models.py            # SQLAlchemy mapped models schema
├── crud.py              # Session CRUD operations and N+1 comparison tests
├── requirements.txt     # Python dependencies mapping
└── README.md
```

## How to Run

1.  Navigate to the directory:
    ```bash
    cd "Module_3_DatabaseIntegration_Solutions/hands_on_6"
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Configure database connection string in `models.py` (e.g. SQLite, PostgreSQL, or MySQL connection string).
4.  Run models mapping to auto-create tables:
    ```bash
    python models.py
    ```
5.  Run CRUD and query logs analysis script:
    ```bash
    python crud.py
    ```
