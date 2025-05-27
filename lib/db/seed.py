from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

# Create authors
a1 = Author("Dennis Muchiri")
a1.save()

a2 = Author("Jane Doe")
a2.save()

# Create magazines
m1 = Magazine("Tech Monthly", "Technology")
m1.save()

m2 = Magazine("Health Weekly", "Health")
m2.save()

# Create articles
art1 = Article("AI in 2025", a1.id, m1.id)
art1.save()

art2 = Article("Wellness Hacks", a2.id, m2.id)
art2.save()

art3 = Article("Tech for All", a1.id, m1.id)
art3.save()

print("✅ Seed data inserted successfully.")
