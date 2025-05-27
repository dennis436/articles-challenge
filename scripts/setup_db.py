import sqlite3
from lib.db.connection import get_connection

def create_tables():
    conn = get_connection()
    with open('lib/db/schema.sql', 'r') as f:
        schema_sql = f.read()
    conn.executescript(schema_sql)
    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

if __name__ == "__main__":
    if os.path.exists('articles.db'):
        print("Warning: articles.db already exists. Delete it if you want to reset the database.")
    else:
        create_tables()
