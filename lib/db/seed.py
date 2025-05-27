from lib.models.author import Author
from lib.models.magazine import Magazine

def seed_data():
    # Clear existing data if needed (optional, depending on your setup)
    
    # Create authors
    author1 = Author(name="Alice Smith")
    author1.save()

    author2 = Author(name="Bob Johnson")
    author2.save()

    author3 = Author(name="Carol Williams")
    author3.save()

    # Create magazines
    mag1 = Magazine(name="Tech Today", category="Technology")
    mag1.save()

    mag2 = Magazine(name="Health Weekly", category="Health")
    mag2.save()

    mag3 = Magazine(name="Travel World", category="Travel")
    mag3.save()

    # Add articles by authors to magazines
    author1.add_article(mag1, "The Future of AI")
    author1.add_article(mag2, "Healthy Eating Habits")
    author1.add_article(mag1, "Advancements in Robotics")

    author2.add_article(mag3, "Top 10 Travel Destinations")
    author2.add_article(mag3, "Budget Travel Tips")
    author2.add_article(mag3, "Travel Safety Guidelines")
    author2.add_article(mag1, "Cybersecurity Essentials")

    author3.add_article(mag2, "Mental Health Awareness")
    author3.add_article(mag2, "Yoga and Wellness")

    print("Seed data created.")

if __name__ == "__main__":
    seed_data()
