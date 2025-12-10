# seed_2.py

from sqlalchemy.orm import Session
from models import engine, Game, User, Review, game_user

# Start session
session = Session(engine)

# Fetch all users and games
users = session.query(User).all()
games = session.query(Game).all()

# Example mapping: assign users to games manually
# You can adjust as needed
if users and games:
    # Alice played Chess and Minecraft
    users[0].games.append(games[0])  # Chess
    users[0].games.append(games[1])  # Minecraft

    # Charlie played Minecraft
    users[2].games.append(games[1])  # Minecraft

    # Bob played Mario Kart
    users[1].games.append(games[2])  # Mario Kart

# Commit changes
session.commit()
print("Many-to-many relationships populated successfully!")

# Close session
session.close()
