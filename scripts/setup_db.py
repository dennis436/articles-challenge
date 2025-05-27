import os
import sys

# Add the parent directory to sys.path so Python can find the 'lib' package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db.connection import get_connection

def setup_db():
    # Remove existing database if it exists
    if os.path.exists('articles.db'):
        os.remove('articles.db')
        print("Old database deleted.")

    conn = get_connection()
    with open('lib/db/schema.sql', 'r') as f:
        schema_sql = f.read()
    conn.executescript(schema_sql)
    conn.commit()
    conn.close()
    print("Database created and schema applied.")

if __name__ == "__main__":
    setup_db()
