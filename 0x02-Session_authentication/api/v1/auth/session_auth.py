#!/usr/bin/env python3
"""the session authentication module"""

from typing import TypeVar
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Session-based authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """initialize a new session"""
        if user_id is None or type(user_id) is not str:
            return None
        self.ID = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[self.ID] = user_id
        return self.ID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """return the user_id associated with the session_id"""
        if session_id is None or type(session_id) is not str:
            return None
        user_id = SessionAuth.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None) -> TypeVar('User'):
        """overload current usr method and get user instance from session
        id in cookie"""
        if request is not None:
            session_id = self.session_cookie(request)
            user_id = self.user_id_for_session_id(session_id)
            user_instance = User.get(user_id)
            return user_instance

    def destroy_session(self, request=None):
        """destroy session method"""
        if request is None:
            return False
        if not self.session_cookie(request):
            return False
        if not self.user_id_for_session_id(self.session_cookie(request)):
            return False
        del self.user_id_by_session_id[self.session_cookie(request)]
        return True
