# MyDatabaseORM

&#x20;

A lightweight, easy-to-use, and flexible Object-Relational Mapper (ORM) that supports multiple databases including **PostgreSQL, MySQL, MSSQL, SQLite, and MongoDB**. Designed for developers who want a simple yet powerful ORM for Python applications.

## Features

✅ Supports multiple databases: **PostgreSQL, MySQL, MSSQL, SQLite, and MongoDB**\
✅ Simple and Pythonic syntax\
✅ Lightweight and fast\
✅ Supports **CRUD operations** (Create, Read, Update, Delete)\
✅ Query Builder for flexible database queries\
✅ MongoDB support with document-based storage\
✅ Easy integration with existing applications\
✅ Open-source and extensible

## Installation

Install the package using `pip`:

```bash
pip install my-database-orm
```

## Quick Start

### 1. Connecting to a Database

```python
from my_database_orm import DatabaseConnection

# Connect to a PostgreSQL database
db = DatabaseConnection(db_type='postgresql', host='localhost', database='test_db', user='user', password='password')
connection = db.connect()
```

### 2. Defining a Model

```python
from my_database_orm import Model

class User(Model):
    pass
```

### 3. Creating a Record

```python
User.insert(connection, name="Alice", age=25)
```

### 4. Fetching Records

```python
from my_database_orm import QueryBuilder

query = QueryBuilder(User).filter(name="Alice").all(connection)
print(query)  # Returns all users named 'Alice'
```

### 5. Updating a Record

```python
User.update(connection, id=1, name="Alice Smith")
```

### 6. Deleting a Record

```python
User.delete(connection, id=1)
```

### 7. MongoDB Support

```python
from my_database_orm.adapters.mongodb_adapter import MongoDBAdapter

mongo = MongoDBAdapter(db_connection=DatabaseConnection(db_type='mongodb', uri='mongodb://localhost:27017')['test_db'], collection_name='users')
mongo.insert({"name": "Alice", "age": 25})
```

## Supported Databases

| Database   | Driver   |
| ---------- | -------- |
| PostgreSQL | psycopg2 |
| MySQL      | pymysql  |
| MSSQL      | pyodbc   |
| SQLite     | sqlite3  |
| MongoDB    | pymongo  |

## Configuration Options

### PostgreSQL/MySQL/MSSQL

```python
DatabaseConnection(
    db_type='postgresql',  # 'mysql', 'mssql'
    host='localhost',
    database='your_db',
    user='your_user',
    password='your_password'
).connect()
```

### SQLite

```python
DatabaseConnection(db_type='sqlite', database='mydb.sqlite3').connect()
```

### MongoDB

```python
DatabaseConnection(db_type='mongodb', uri='mongodb://localhost:27017').connect()
```

## Advanced Querying

Using the Query Builder:

```python
query = QueryBuilder(User).filter(age=25).all(connection)
print(query)
```

Updating multiple records:

```python
QueryBuilder(User).filter(age=25).update(name="Updated Name").execute(connection)
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License

This project is licensed under the **MIT License**.

---

📌 **Author:** Verkyav Peter\
🐍 **GitHub:** [github.com/cleancodelover](https://github.com/cleancodelover)\
📧 **Contact:** [verkyavpeter@gmail.com](mailto\:verkyavpeter@gmail.com)

