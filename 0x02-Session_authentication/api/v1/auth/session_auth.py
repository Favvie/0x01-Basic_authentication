#!/usr/bin/env python3
"""the session authentication module"""

from api.v1.auth.auth import Auth
import uuid


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
        if session_id is None or type(session_id) is not str:
            return None
        user_id = SessionAuth.user_id_by_session_id.get(session_id)
        return user_id
