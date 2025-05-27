# test/test_magazine.py
import pytest
from lib.models.magazine import Magazine

def test_magazine_has_name_and_category():
    magazine = Magazine("Science Weekly", "Science")
    assert magazine.name == "Science Weekly"
    assert magazine.category == "Science"
