# test/test_article.py

import pytest
from lib.models.article import Article, Author, Magazine

def test_article_has_title():
    author = Author("John Doe")
    magazine = Magazine("Tech Today", "Technology")
    article = Article("The Rise of AI", author, magazine)

    assert article.title == "The Rise of AI"
