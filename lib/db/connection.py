import sqlite3
import os
import sys

DB_FILE = 'articles.db'

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_connection()
    with open('lib/db/schema.sql', 'r') as f:
        schema_sql = f.read()
    conn.executescript(schema_sql)
    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'reset':
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)
            print(f"Deleted existing {DB_FILE}")
        create_tables()
    else:
        print("Usage: python lib/db/connection.py reset")
