# Game Reviews Project

**Author:** Your Name  
**Project:** SQLAlchemy Many-to-Many Relationships  

---

## Project Overview

This project demonstrates the use of **SQLAlchemy ORM** to model **one-to-many** and **many-to-many** relationships in a games and reviews domain. It includes three main models:

1. **Game** – Represents a game with a title, genre, platform, and price.  
2. **User** – Represents a user who can review games.  
3. **Review** – Represents a user's review of a game, including a score and comment.  

### Relationships

- **One-to-Many**
  - A `Game` has many `Review`s.
  - A `User` has many `Review`s.
  - Each `Review` belongs to a `Game` and a `User`.

- **Many-to-Many**
  - A `Game` has many `User`s through reviews.
  - A `User` has many `Game`s through reviews.
  - Implemented using an **association table** `game_user`.

---

## Folder Structure

