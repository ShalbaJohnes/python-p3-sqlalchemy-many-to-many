from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table, func
from sqlalchemy.orm import relationship, backref, declarative_base

# --- Engine ---
engine = create_engine('sqlite:///many_to_many.db', echo=True)  # echo=True shows SQL logs

# --- Base ---
Base = declarative_base()

# --- Association table for many-to-many relationship between Games and Users ---
game_user = Table(
    'game_users',
    Base.metadata,
    Column('game_id', ForeignKey('games.id'), primary_key=True),
    Column('user_id', ForeignKey('users.id'), primary_key=True)
)

# --- Game Model ---
class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    platform = Column(String)
    price = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Relationships
    users = relationship('User', secondary=game_user, back_populates='games')
    reviews = relationship('Review', backref=backref('game'))

    def __repr__(self):
        return f'Game(id={self.id}, title="{self.title}", platform="{self.platform}")'

# --- User Model ---
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Relationships
    games = relationship('Game', secondary=game_user, back_populates='users')
    reviews = relationship('Review', backref=backref('user'))

    def __repr__(self):
        return f'User(id={self.id}, name="{self.name}")'

# --- Review Model ---
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    comment = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    game_id = Column(Integer, ForeignKey('games.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'Review(id={self.id}, score={self.score}, game_id={self.game_id}, user_id={self.user_id})'
