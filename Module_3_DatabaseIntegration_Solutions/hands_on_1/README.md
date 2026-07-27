# Hands-On 01: Database Schema Design, DDL & Normalization

This folder contains the database schema design and Data Definition Language (DDL) implementation for the college registration system `college_db`.

## Topics Covered
*   Database Schema Design
*   Entity Relationship (ER) Constraints
*   Normalisation rules (1NF, 2NF, 3NF compliance checking)
*   DDL statements (CREATE TABLE, ALTER TABLE, DROP TABLE, CHECK constraints)

## Folder Structure

```text
hands_on_1/
├── hands_on_1.sql       # DDL Schema scripts, 3NF comments, and Alter statements
└── README.md            # Dedicated documentation
```

## How to Execute

1.  Connect to your database engine (PostgreSQL or MySQL client).
2.  Create the database:
    ```sql
    CREATE DATABASE college_db;
    ```
3.  Run the SQL script file using your client or CLI:
    ```bash
    # For PostgreSQL
    psql -U username -d college_db -f hands_on_1.sql

    # For MySQL
    mysql -u username -p college_db < hands_on_1.sql
    ```
