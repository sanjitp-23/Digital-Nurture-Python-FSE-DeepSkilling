# Hands-On 05: MongoDB Document Modelling, CRUD & Aggregations

This folder contains exercises for modelling Course Feedback unstructured data using MongoDB documents, performing CRUD operations, and building aggregation pipelines.

## Topics Covered
*   Documents schema design and collection setups
*   MongoDB shell CRUD (find, updateOne/updateMany, deleteMany)
*   Aggregation pipelines ($match, $group, $sort, $project, $unwind, $round)
*   Indexing and execution plans check (IXSCAN vs COLLSCAN)

## Folder Structure

```text
hands_on_5/
├── mongodb_queries.js   # MongoDB queries & aggregations scripts
└── README.md
```

## How to Run

1.  Connect to your MongoDB Community Server instance using `mongosh` CLI or MongoDB Compass.
2.  Switch/create database:
    ```javascript
    use college_nosql;
    ```
3.  Run the collection initialization, CRUD operations, and aggregation queries. You can load or copy commands directly from `mongodb_queries.js`.
