# Articles Challenge

This project implements a simple content management system featuring Authors, Magazines, and Articles.  
It uses SQLite for data storage and Python classes to interact with the database.

## Features

- Create, read, update, and delete (CRUD) operations for Authors, Magazines, and Articles  
- Retrieve articles by author or magazine  
- Track contributors and article titles per magazine  
- Fully tested with `pytest`

## Requirements

- Python 3.8+  
- SQLite3  
- `pytest` (for running tests)

## Setup

1. Clone the repository:  
   ```bash
   git clone <your-repo-url>
   cd articles-challenge
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# project structure
lib/
  models/
    author.py
    magazine.py
    article.py
  db/
    connection.py
test/
  test_author.py
  test_magazine.py
  test_article.py
  test_models.py
README.md

# usage
from lib.models.author import Author

author = Author(name="Jane Doe")
author.save()

found = Author.find_by_id(author.id)
print(found.name)  # Outputs: Jane Doe

# license
Author (Muchiri Dennis)
MIT License

