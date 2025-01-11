from src.db import PostgresDB
import os

def insert_user_data():
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
        
        # Example user data
        users_to_insert = [
            {
                "name": "John Doe",
                "email": "john@example.com"
            },
            {
                "name": "Jane Smith",
                "email": "jane@example.com"
            },
            {
                "name": "Bob Wilson",
                "email": "bob@example.com"
            }
        ]
        
        # Insert each user
        for user in users_to_insert:
            db.insert_data("users", user)
            
        # Verify insertion by selecting all records
        print("\nRetrieving all users:")
        results = db.select_all("users")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Created: {row[3]}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close connection
        db.disconnect()

if __name__ == "__main__":
    insert_user_data()