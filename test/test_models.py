from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
import pytest
def test_author():
    # Create and save an author
    author = Author("Jane Doe")
    author.save()
    print(f"Saved author with ID: {author.id}")

    # Find by ID
    found_author = Author.find_by_id(author.id)
    assert found_author is not None and found_author.name == "Jane Doe"

    # Find by name
    found_author_by_name = Author.find_by_name("Jane Doe")
    assert found_author_by_name is not None and found_author_by_name.id == author.id

    print("Author tests passed.")

def test_magazine():
    # Create and save a magazine
    mag = Magazine("Tech Today", "Technology")
    mag.save()
    print(f"Saved magazine with ID: {mag.id}")

    # Find by ID
    found_mag = Magazine.find_by_id(mag.id)
    assert found_mag is not None and found_mag.name == "Tech Today"

    # Find by name
    found_mag_by_name = Magazine.find_by_name("Tech Today")
    assert found_mag_by_name is not None and found_mag_by_name.id == mag.id

    # Find by category
    mags = Magazine.find_by_category("Technology")
    assert any(m.id == mag.id for m in mags)

    print("Magazine tests passed.")

def test_article():
    # Setup author and magazine first
    author = Author("John Smith")
    author.save()
    magazine = Magazine("Science Weekly", "Science")
    magazine.save()

    # Create and save an article
    article = Article("New Discoveries", author.id, magazine.id)
    article.save()
    print(f"Saved article with ID: {article.id}")

    # Find article by ID
    found_article = Article.find_by_id(article.id)
    assert found_article is not None and found_article.title == "New Discoveries"

    # Find by title
    found_by_title = Article.find_by_title("New Discoveries")
    assert found_by_title is not None and found_by_title.title == "New Discoveries"

    # Find by author
    articles_by_author = Article.find_by_author(author.id)
    assert any(a.id == article.id for a in articles_by_author)

    # Find by magazine
    articles_by_magazine = Article.find_by_magazine(magazine.id)
    assert any(a.id == article.id for a in articles_by_magazine)

    # Test related methods
    assert found_article.author().id == author.id
    assert found_article.magazine().id == magazine.id

    print("Article tests passed.")

if __name__ == "__main__":
    test_author()
    test_magazine()
    test_article()
    print("All tests passed!")
