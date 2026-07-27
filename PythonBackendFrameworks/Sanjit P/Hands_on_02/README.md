# Hands-On 02: Django Models, ORM & Admin Interface

This folder contains the implementation for Hands-On 02, focusing on defining relational models, performing ORM queries, and configuring the Django Admin dashboard.

## Topics Covered
*   Django Models Definition
*   Database Schema Migrations
*   Django Admin Interface Customization
*   Django ORM Queries (CRUD, Filter, Annotation, select_related, F-expressions)

## Folder Structure

```text
Hands_on_02/
└── coursemanager/
    ├── coursemanager/     # Configuration package
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── courses/           # Core courses application
    │   ├── migrations/    # Schema change scripts
    │   ├── admin.py       # Custom ModelAdmin (CourseAdmin)
    │   ├── models.py      # Department, Course, Student, Enrollment models
    │   ├── ORM.sql        # Django ORM reference queries (Tasks 17-20)
    │   ├── views.py       # CRUD REST views
    │   └── ...
    ├── db.sqlite3         # SQLite Database
    └── manage.py
```

## How to Run

1.  Navigate to the `coursemanager` directory:
    ```bash
    cd "Python Backend Framework Solutions/Sanjit P/Hands_on_02/coursemanager"
    ```
2.  Install dependencies:
    ```bash
    pip install django djangorestframework
    ```
3.  Run migrations:
    ```bash
    python manage.py migrate
    ```
4.  Start server:
    ```bash
    python manage.py runserver
    ```
5.  Open Django admin at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in using credentials created via `createsuperuser`.
