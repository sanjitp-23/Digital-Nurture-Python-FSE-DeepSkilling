# Hands-On 02: DML, Joins & Aggregations

This folder contains DML scripts for inserting sample records, querying tables, filtering results, executing joins, and computing aggregated metrics.

## Topics Covered
*   DML CRUD queries (INSERT, UPDATE, DELETE)
*   Single table query patterns (ORDER BY, LIKE, BETWEEN)
*   Multi-table SQL JOINS (INNER, LEFT OUTER)
*   Aggregate functions and grouping (GROUP BY, HAVING, COUNT, AVG, ROUND)

## Folder Structure

```text
hands_on_2/
├── hands_on_2.sql       # DML Insertion and SELECT Query statements
└── README.md
```

## How to Execute

1.  Connect to your active SQL server instance.
2.  Select `college_db` database.
3.  Execute the query script:
    ```bash
    # For PostgreSQL
    psql -U username -d college_db -f hands_on_2.sql

    # For MySQL
    mysql -u username -p college_db < hands_on_2.sql
    ```
