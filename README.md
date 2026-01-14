# RDBMSlite
#### Overview
This project is a minimal educational relational database management system (RDBMS) implemented to demonstrate core database concepts such as table definitions, CRUD operations, indexing, and joins.

It is not intended to be a production-ready database, but rather a focused exploration of how relational databases work internally.

#### High-Level Architecture
The system is composed of the following layers:

1. REPL Interface
   - Accepts SQL-like commands interactively

2. Parser
   - Converts user input into structured commands (AST)

3. Executor
   - Applies CRUD operations and joins based on parsed commands

4. Storage Engine
   - Manages tables, rows, and indexes in memory or files

Flow: REPL → Parser → Executor → Storage

#### Supporeted Features
1. Data Types
>> INT, 
>> TEXT,
>> BOOL,
2. Constraints
>> Primary Key
3. SQL Operations
>> CREATE TABLE
>> SELECT
>> INSERT
4. Inner Joins
>> INNER JOIN on equality conditions only
5. Indexing
>> - Hash-based index on PRIMARY KEY and UNIQUE columns
#### Limitations
The following features are intentionally not implemented:
- Transactions and ACID guarantees
- Concurrency control
- Query optimization
- Complex SQL syntax (GROUP BY, subqueries, etc.)
- Disk-based B-tree indexing.

These were excluded to keep the system small, understandable, and implementable
within a limited timeframe while maintaining correctness.

#### Data Model
Each table consists of:
- A schema (column names, types, constraints)
- A collection of rows stored as key-value maps
- Optional indexes for fast lookup

###### example

Row:
{
  "id": 1,
  "email": "user@example.com",
  "active": true
}



