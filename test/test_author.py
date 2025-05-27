import pytest
from lib.models.author import Author
from lib.db.connection import get_connection

@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    """Reset the database schema before each test to ensure isolation."""
    conn = get_connection()
    with open('lib/db/schema.sql') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    yield
    # Optional: Add teardown logic if using a temporary DB file

def test_create_and_find_author():
    """Test saving an author and retrieving them by ID."""
    author = Author(name="Jane Doe")
    author.save()

    assert author.id is not None, "Author ID should be set after saving."

    found_author = Author.find_by_id(author.id)
    assert found_author is not None, "Author should be found by ID."
    assert found_author.name == "Jane Doe", "Author name should match saved value."

def test_find_by_name():
    """Test finding an author by name."""
    author = Author(name="Alice")
    author.save()

    found = Author.find_by_name("Alice")
    assert found is not None, "Author should be found by name."
    assert found.name == "Alice", "Author name should match the search value."
