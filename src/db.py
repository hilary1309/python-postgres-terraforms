import psycopg2
from psycopg2 import Error
from typing import List, Dict, Any
import os

class PostgresDB:
    def __init__(self, dbname: str, user: str, password: str, host: str = "localhost", port: str = "5432"):
        self.conn_params = {
            "dbname": dbname,
            "user": user,
            "password": password,
            "host": host,
            "port": port
        }
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(**self.conn_params)
            self.cur = self.conn.cursor()
            print("Successfully connected to PostgreSQL")
        except Error as e:
            print(f"Error connecting to PostgreSQL: {e}")
            raise

    def disconnect(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed")

    def create_table(self, table_name: str, columns: Dict[str, str]):
        try:
            columns_def = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
            create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})"
            self.cur.execute(create_query)
            self.conn.commit()
            print(f"Table {table_name} created successfully")
        except Error as e:
            print(f"Error creating table: {e}")
            self.conn.rollback()

    def insert_data(self, table_name: str, data: Dict[str, Any]):
        try:
            columns = ", ".join(data.keys())
            values = ", ".join(["%s" for _ in data])
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            self.cur.execute(query, list(data.values()))
            self.conn.commit()
            print("Data inserted successfully")
        except Error as e:
            print(f"Error inserting data: {e}")
            self.conn.rollback()

    def select_all(self, table_name: str) -> List[tuple]:
        try:
            self.cur.execute(f"SELECT * FROM {table_name}")
            return self.cur.fetchall()
        except Error as e:
            print(f"Error selecting data: {e}")
            return []        