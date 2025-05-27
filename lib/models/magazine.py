from lib.db.connection import get_connection
from contextlib import closing 

class Magazine:
    def __init__(self, name, category, id=None):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        if not category or not isinstance(category, str):
            raise ValueError("Category must be a non-empty string.")
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO magazines (name, category) VALUES (?, ?)",
                (self.name, self.category)
            )
            conn.commit()
            self.id = cursor.lastrowid

    @classmethod
    def find_by_id(cls, id):
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
            row = cursor.fetchone()
            return cls(row["name"], row["category"], row["id"]) if row else None

    @classmethod
    def find_by_name(cls, name):
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
            row = cursor.fetchone()
            return cls(row["name"], row["category"], row["id"]) if row else None

    @classmethod
    def find_by_category(cls, category):
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines WHERE category = ?", (category,))
            rows = cursor.fetchall()
            return [cls(row["name"], row["category"], row["id"]) for row in rows]

    def articles(self):
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
            return cursor.fetchall()

    def contributors(self):
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT DISTINCT a.* FROM authors a
                JOIN articles ar ON ar.author_id = a.id
                WHERE ar.magazine_id = ?
            """, (self.id,))
            return cursor.fetchall()

    def article_titles(self):
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT title FROM articles
                WHERE magazine_id = ?
            """, (self.id,))
            rows = cursor.fetchall()
            return [row["title"] for row in rows]

    def contributing_authors(self):
        with closing (get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT a.*, COUNT(ar.id) as article_count FROM authors a
                JOIN articles ar ON ar.author_id = a.id
                WHERE ar.magazine_id = ?
                GROUP BY a.id
                HAVING article_count > 2
            """, (self.id,))
            return cursor.fetchall()

    def __repr__(self):
        return f"<Magazine id={self.id} name='{self.name}' category='{self.category}'>"
