
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Fixture(Base):
    __tablename__ = "fixtures"
    id = Column(Integer, primary_key=True, index=True)
    home_team = Column(String)
    away_team = Column(String)
    match_date = Column(String)

class Pick(Base):
    __tablename__ = "picks"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    fixture_id = Column(Integer, ForeignKey("fixtures.id"))
    team_chosen = Column(String)
