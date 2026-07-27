# Hands-On 10: Microservices Architecture — Concepts & Decomposition

This folder contains the implementation for Hands-On 10, decomposing the monolith Course Management app into independent Microservices, implementing synchronous inter-service communication, and configuring an API Gateway.

## Topics Covered
*   Monolith vs. Microservices architecture
*   Service decomposition boundaries
*   Synchronous inter-service HTTP calls (using requests)
*   API Gateway pattern configuration

## Folder Structure

```text
Hands_on_10/
└── Handson_10/
    ├── course_service/    # Course and Department management service (Port 5001)
    │   ├── app.py
    │   └── requirements.txt
    ├── student_service/   # Student and Enrollment management service (Port 5002)
    │   ├── app.py
    │   └── requirements.txt
    ├── gateway/           # Flask API Gateway proxy router (Port 5000)
    │   ├── app.py
    │   └── requirements.txt
    └── README.md          # Dedicated microservices trade-offs notes
```

## How to Run

1.  **Start Course Service (Port 5001)**:
    ```bash
    cd "Python Backend Framework Solutions/Sanjit P/Hands_on_10/Handson_10/course_service"
    pip install -r requirements.txt
    python app.py
    ```
2.  **Start Student Service (Port 5002)**:
    ```bash
    cd "Python Backend Framework Solutions/Sanjit P/Hands_on_10/Handson_10/student_service"
    pip install -r requirements.txt
    python app.py
    ```
3.  **Start API Gateway (Port 5000)**:
    ```bash
    cd "Python Backend Framework Solutions/Sanjit P/Hands_on_10/Handson_10/gateway"
    pip install -r requirements.txt
    python app.py
    ```
4.  **Test Gateway Routing**:
    *   List courses via gateway proxy: `GET http://127.0.0.1:5000/api/courses/`
    *   Enroll a student via gateway: `POST http://127.0.0.1:5000/api/students/1/enroll` (This calls Student Service, which in turn performs an internal inter-service call to Course Service on port 5001 to verify the course existence).
