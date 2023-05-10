#!/usr/bin/env python3
"""User"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    """User Model"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

    def __init__(self, email, hashed_password):
        """initialization"""
        self.email = email
        self.hashed_password = hashed_password

    def __repr__(self):
        return f"{self.id} {self.email} {self.hashed_password}"
