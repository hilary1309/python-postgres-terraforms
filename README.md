# PostgresDB Python Wrapper

## Overview
This project provides a Python wrapper class, `PostgresDB`, for managing PostgreSQL database connections and operations. It simplifies tasks like connecting to the database, creating tables, and safely disconnecting.

## Prerequisites
- Python 3.6+
- PostgreSQL
- `psycopg2` library (install with `pip install psycopg2`)

## Usage

### Example Code
```python
from db import PostgresDB
import os

# Initialize database connection
db = PostgresDB(
    dbname="project_one",
    user="admin",
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST', 'localhost')
)

try:
    # Connect to database
    db.connect()
    
    # Create a table
    columns = {
        "id": "SERIAL PRIMARY KEY",
        "name": "VARCHAR(100)",
        "email": "VARCHAR(100)",
        "created_at": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
    }
    db.create_table("users", columns)
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close connection
    db.disconnect()
```
# PostgreSQL Setup Instructions

## Connect to PostgreSQL
```bash
# Connect via psql command line
psql -U postgres

# If using Mac with Homebrew
psql postgres
```

## Create Database and User
```sql
-- Create new database
CREATE DATABASE project_one;

-- Create new user
CREATE USER admin WITH PASSWORD 'your_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE project_one TO admin;
```



## Methods

### `connect()`
Establishes a connection to the PostgreSQL database.

### `create_table(table_name, columns)`
Creates a table with the specified name and column definitions.

### `disconnect()`
Closes the database connection and cursor gracefully.

## License
This project is licensed under the MIT License.


