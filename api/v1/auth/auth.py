#!/usr/bin/env/python3
"""the authentication module"""

from flask import request
from typing import TypeVar, List


class Auth:
    """The base authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """check if the path requires authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """checks if the request has an authorization header"""
        return None

    def current_user(user, request=None) -> TypeVar('User'):
        """check if there is a current user"""
        return None
