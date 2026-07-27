# Hands-On 03: Django REST Views, URL Routing & Forms

This folder contains the implementation for Hands-On 03, building API endpoints using Django REST Framework (DRF) serializing systems, APIView, ViewSets, and Routers.

## Topics Covered
*   DRF ModelSerializers
*   DRF APIViews (GET, POST, PUT, DELETE)
*   DRF ViewSets and DefaultRouters
*   Custom Actions on ViewSets (`@action`)

## Folder Structure

```text
Hands_on_03/
└── coursemanager/
    ├── coursemanagement/  # Django settings & URL configuration
    ├── course/            # App containing models & API endpoints
    │   ├── serializers.py # Serializers for Dept, Course, Student, Enrollment
    │   ├── views.py       # APIView & ModelViewSet implementations
    │   ├── urls.py        # Router routing registration
    │   └── models.py
    └── manage.py
```

## How to Run

1.  Navigate to the `coursemanager` directory:
    ```bash
    cd "Python Backend Framework Solutions/Sanjit P/Hands_on_03/coursemanager"
    ```
2.  Install dependencies:
    ```bash
    pip install django djangorestframework
    ```
3.  Start server:
    ```bash
    python manage.py runserver
    ```
4.  Interact with endpoints via browser or API clients:
    *   List courses: `GET http://127.0.0.1:8000/api/courses/`
    *   Enrolled students list custom action: `GET http://127.0.0.1:8000/api/courses/{id}/students/`
