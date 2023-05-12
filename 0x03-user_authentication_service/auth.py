#!/usr/bin/env python3
"""auth module"""
from bcrypt import hashpw, gensalt
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """hash password string using bcrypt.hashpw"""
    bpassword = bytes(password, 'utf-8')
    salt = gensalt()
    hash = hashpw(bpassword, salt)
    return hash


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register user using a hashed password to database"""
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashedPwd = _hash_password(password)
            # user = User(email, hashedPwd)
            user = self._db.add_user(email, hashedPwd)
        return user
