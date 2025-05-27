import sqlite3
import os
import sys

DB_FILENAME = 'database.db'
SCHEMA_PATH = 'lib/db/schema.sql'

def get_connection():
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    print(f"Checking if schema file exists at: {SCHEMA_PATH}")
    if not os.path.exists(SCHEMA_PATH):
        print(f"Error: Schema file '{SCHEMA_PATH}' not found.")
        return

    with open(SCHEMA_PATH, 'r') as f:
        schema_sql = f.read()

    print(f"Schema file read, length: {len(schema_sql)} characters")

    if not schema_sql.strip():
        print("Error: Schema file is empty.")
        return

    conn = get_connection()
    print("Opened database connection")

    conn.executescript(schema_sql)
    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

if __name__ == "__main__":
    print(f"Database file exists? {os.path.exists(DB_FILENAME)}")
    if os.path.exists(DB_FILENAME):
        if len(sys.argv) > 1 and sys.argv[1].lower() == 'reset':
            print(f"Deleting existing database file: {DB_FILENAME}")
            os.remove(DB_FILENAME)
            create_tables()
        else:
            print(f"Warning: '{DB_FILENAME}' already exists. To reset, run:\n  python {sys.argv[0]} reset")
    else:
        create_tables()
