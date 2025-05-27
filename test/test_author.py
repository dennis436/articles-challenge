# test/test_author.py
import pytest
from lib.models.author import Author

def test_author_has_name():
    author = Author("Jane Smith")
    assert author.name == "Jane Smith"
    author.save()  # <- Fixed indentation
