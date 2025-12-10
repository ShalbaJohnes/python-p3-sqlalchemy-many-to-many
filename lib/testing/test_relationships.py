import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from models import engine, Game, User, Review
from sqlalchemy.orm import Session

# Start a session
session = Session(engine)

print("=== Games and their Users ===")
games = session.query(Game).all()
for game in games:
    user_names = [user.name for user in game.users]
    print(f"{game.title}: Users -> {user_names}")

print("\n=== Users and their Games ===")
users = session.query(User).all()
for user in users:
    game_titles = [game.title for game in user.games]
    print(f"{user.name}: Games -> {game_titles}")

print("\n=== Reviews ===")
reviews = session.query(Review).all()
for review in reviews:
    print(f"{review.user.name} reviewed {review.game.title} - Score: {review.score}, Comment: {review.comment}")

# Close session
session.close()
