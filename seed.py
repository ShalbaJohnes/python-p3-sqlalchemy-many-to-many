from sqlalchemy.orm import Session
from models import engine, Base, Game, User, Review

# Create all tables in the database (if they don't exist)
Base.metadata.create_all(engine)

# Start a session
session = Session(engine)

# --- Create sample games ---
game1 = Game(title="Chess", genre="Strategy", platform="Board", price=0)
game2 = Game(title="Mario Kart", genre="Racing", platform="Nintendo", price=50)
game3 = Game(title="Minecraft", genre="Sandbox", platform="PC", price=30)

# --- Create sample users ---
user1 = User(name="Alice")
user2 = User(name="Bob")
user3 = User(name="Charlie")

# --- Create sample reviews ---
review1 = Review(score=5, comment="Amazing strategy!", game=game1, user=user1)
review2 = Review(score=4, comment="Fun racing game", game=game2, user=user2)
review3 = Review(score=5, comment="Creative and fun", game=game3, user=user1)
review4 = Review(score=3, comment="Good, but buggy", game=game3, user=user3)

# Add everything to the session
session.add_all([game1, game2, game3, user1, user2, user3, review1, review2, review3, review4])

# Commit to save in the database
session.commit()

# Close session
session.close()

print("Database seeded successfully!")
