from src.db import PostgresDB
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