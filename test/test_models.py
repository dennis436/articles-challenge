import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Clean tables before running tests
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()

    yield  # Run tests

    # Clean up after tests
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()

def test_author_crud():
    author = Author(name="Test Author")
    author.save()
    assert author.id is not None

    found = Author.find_by_id(author.id)
    assert found is not None
    assert found.name == "Test Author"

    # Update author
    author.name = "Updated Author"
    author.save()

    updated = Author.find_by_id(author.id)
    assert updated.name == "Updated Author"

def test_magazine_crud():
    # Notice: Added 'category' argument to fix NOT NULL constraint error
    magazine = Magazine(name="Test Magazine", category="Tech")
    magazine.save()
    assert magazine.id is not None

    found = Magazine.find_by_id(magazine.id)
    assert found is not None
    assert found.name == "Test Magazine"
    assert found.category == "Tech"

    # Update magazine
    magazine.name = "Updated Magazine"
    magazine.category = "Science"  # Update category too
    magazine.save()

    updated = Magazine.find_by_id(magazine.id)
    assert updated.name == "Updated Magazine"
    assert updated.category == "Science"

def test_article_crud():
    # Setup author and magazine for foreign keys (with category for magazine)
    author = Author(name="Article Author")
    author.save()
    magazine = Magazine(name="Article Magazine", category="Lifestyle")
    magazine.save()

    article = Article(title="Test Article", author_id=author.id, magazine_id=magazine.id)
    article.save()
    assert article.id is not None

    found = Article.find_by_id(article.id)
    assert found is not None
    assert found.title == "Test Article"
    assert found.author_id == author.id
    assert found.magazine_id == magazine.id

    # Update article
    article.title = "Updated Article"
    article.save()

    updated = Article.find_by_id(article.id)
    assert updated.title == "Updated Article"

def test_article_find_by_author_and_magazine():
    # Setup author and magazine (with category)
    author = Author(name="Find Test Author")
    author.save()
    magazine = Magazine(name="Find Test Magazine", category="Business")
    magazine.save()

    # Create multiple articles
    a1 = Article(title="Article One", author_id=author.id, magazine_id=magazine.id)
    a1.save()
    a2 = Article(title="Article Two", author_id=author.id, magazine_id=magazine.id)
    a2.save()

    # Find articles by author
    articles_by_author = Article.find_by_author(author.id)
    assert len(articles_by_author) >= 2
    titles = [a.title for a in articles_by_author]
    assert "Article One" in titles and "Article Two" in titles

    # Find articles by magazine
    articles_by_magazine = Article.find_by_magazine(magazine.id)
    assert len(articles_by_magazine) >= 2
    titles_mag = [a.title for a in articles_by_magazine]
    assert "Article One" in titles_mag and "Article Two" in titles_mag
