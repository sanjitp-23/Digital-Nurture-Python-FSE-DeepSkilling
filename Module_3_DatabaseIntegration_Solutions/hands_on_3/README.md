# Hands-On 03: Subqueries, Views & Transactions

This folder contains SQL queries for advanced data grouping, reusable view structures, stored procedures/functions definition, and transaction safety management.

## Topics Covered
*   Correlated & non-correlated subqueries
*   Virtual view structures with integrity checks (`WITH CHECK OPTION`)
*   Stored Procedures (MySQL) & PL/pgSQL Functions (PostgreSQL)
*   Transactional commits, rollbacks, and mid-transaction checkpoints (`SAVEPOINT`)

## Folder Structure

```text
hands_on_3/
├── hands_on_3.sql       # SQL Views, Subqueries, Procedures, and Transactions Script
└── README.md
```

## How to Execute

1.  Connect to your relational server client.
2.  Use the `college_db` database.
3.  Run the script to register procedures and test rollback scenarios:
    ```bash
    # For PostgreSQL
    psql -U username -d college_db -f hands_on_3.sql

    # For MySQL
    mysql -u username -p college_db < hands_on_3.sql
    ```
