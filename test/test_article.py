import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown_db():
    # Setup: Create tables and seed test data
    conn = get_connection()
    cursor = conn.cursor()

    # Clean tables before tests
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")

    # Insert test authors
    cursor.execute("INSERT INTO authors (name) VALUES ('Author One')")
    cursor.execute("INSERT INTO authors (name) VALUES ('Author Two')")

    # Insert test magazines WITH category to avoid NOT NULL error
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Magazine One", "Tech"))
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Magazine Two", "Science"))

    conn.commit()

    yield  # tests run here

    # Teardown (optional)
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()

def test_create_and_find_article():
    # Assume authors and magazines with id 1 exist from fixture
    article = Article(title="Test Article", author_id=1, magazine_id=1)
    article.save()
    assert article.id is not None

    found = Article.find_by_id(article.id)
    assert found is not None
    assert found.title == "Test Article"
    assert found.author_id == 1
    assert found.magazine_id == 1

def test_find_by_author():
    # Create two articles for author 1 and one for author 2
    a1 = Article(title="Article A1", author_id=1, magazine_id=1)
    a1.save()
    a2 = Article(title="Article A2", author_id=1, magazine_id=2)
    a2.save()
    a3 = Article(title="Article B1", author_id=2, magazine_id=1)
    a3.save()

    author1_articles = Article.find_by_author(1)
    assert len(author1_articles) >= 2
    titles = [a.title for a in author1_articles]
    assert "Article A1" in titles and "Article A2" in titles

def test_find_by_magazine():
    mag_articles = Article.find_by_magazine(1)
    assert len(mag_articles) >= 1
    titles = [a.title for a in mag_articles]
    assert any(t in titles for t in ["Article A1", "Article B1"])
