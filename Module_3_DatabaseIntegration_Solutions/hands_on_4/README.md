# Hands-On 04: Query Optimization & the N+1 Query Problem

This folder contains SQL optimization strategies, index creation statements, EXPLAIN query plan analysis, and a Python simulation addressing the N+1 select query problem.

## Topics Covered
*   EXPLAIN and EXPLAIN ANALYZE commands
*   Indexing strategies (B-Tree, Composite, and Partial indexes)
*   The ORM N+1 query problem and its impact on performance
*   Optimizing fetches using SQL JOIN operations in Python

## Folder Structure

```text
hands_on_4/
├── python/
│   ├── n_plus_one_demo.py # Lazy loading simulation executing 13 queries
│   └── optimized_join.py  # Eager loading executing 1 single JOIN query
├── hands_on_4.sql         # Index creations & EXPLAIN plans analysis
└── README.md
```

## How to Run the Python Simulation

1.  Setup your database environment and migrate the schema.
2.  Install database adapter dependency (e.g. `mysql-connector-python` or `psycopg2` depending on database target).
3.  Run the N+1 problem simulation:
    ```bash
    python python/n_plus_one_demo.py
    ```
4.  Run the optimized join query script:
    ```bash
    python python/optimized_join.py
    ```
5.  Observe the time and query count difference in console logs.
