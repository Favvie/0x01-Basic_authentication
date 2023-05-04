#!/usr/bin/env python3
"""the authentication module"""

from flask import request
from typing import TypeVar, List


class Auth:

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """check if the path requires authentication"""
        if path is None or excluded_paths is None:
            return True
        if path.endswith('/'):
            pass
        else:
            path = path + "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """checks if the request has an authorization header"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(user, request=None) -> TypeVar('User'):
        """check if there is a current user"""
        return None
