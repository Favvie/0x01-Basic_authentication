#!/usr/bin/env python3
"""auth module"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """hash password string using bcrypt.hashpw"""
    bpassword = bytes(password, 'utf-8')
    salt = gensalt()
    hash = hashpw(bpassword, salt)
    return hash
