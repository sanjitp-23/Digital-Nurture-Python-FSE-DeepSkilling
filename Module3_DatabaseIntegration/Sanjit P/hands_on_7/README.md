# Hands-On 07: Migrations & Versioning — Alembic

This folder contains exercises for setting up version control for database schemas using Alembic, applying upgrades/downgrades, and generating incremental schema migrations.

## Topics Covered
*   Initializing Alembic migrations history
*   Autogenerating migrations from SQLAlchemy metadata
*   Applying incremental upgrades and rolling back using downgrade revisions
*   Tracking applied versions using the `alembic_version` metadata table

## Folder Structure

```text
hands_on_7/
├── migrations/          # Alembic scripts version history
├── alembic.ini          # Alembic database connections configurations
├── database.py          # Session and DB engine mappings
├── models.py            # SQLAlchemy schema models definitions
├── crud.py              # Test operations helper
├── requirements.txt     # Packages lists
└── README.md
```

## How to Run

1.  Navigate to the directory:
    ```bash
    cd "Module_3_DatabaseIntegration_Solutions/hands_on_7"
    ```
2.  Install packages:
    ```bash
    pip install -r requirements.txt
    ```
3.  Configure `sqlalchemy.url` inside `alembic.ini`.
4.  Apply migrations:
    ```bash
    # Apply all migrations to latest version
    alembic upgrade head

    # Rollback one migration revision
    alembic downgrade -1

    # Rollback database to initial clean state
    alembic downgrade base
    ```
