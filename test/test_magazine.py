import pytest
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Clean magazines table
    cursor.execute("DELETE FROM magazines")
    conn.commit()

    yield

    # Cleanup
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()

def test_create_and_find_magazine():
    magazine = Magazine(name="New Magazine", category="Tech")
    magazine.save()
    assert magazine.id is not None

    found = Magazine.find_by_id(magazine.id)
    assert found is not None
    assert found.name == "New Magazine"
    assert found.category == "Tech"

def test_update_magazine():
    magazine = Magazine(name="Old Name", category="Lifestyle")
    magazine.save()
    magazine.name = "Updated Name"
    magazine.save()

    found = Magazine.find_by_id(magazine.id)
    assert found.name == "Updated Name"
    assert found.category == "Lifestyle"
