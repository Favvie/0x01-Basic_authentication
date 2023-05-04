#!/usr/bin/env python3
"""Basic authentication module"""


from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic authentication class"""
    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        """extract the base64 encoding from auth header"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """decode a base64 encoding into utf-8"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            value = base64.b64decode(base64_authorization_header)
        except Exception:
            return None
        value = value.decode('utf-8')
        return value

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> Tuple[str, str]:
        """extract user credentials from decoded base64 str"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        username = decoded_base64_authorization_header.split(":")[0]
        userpwd = decoded_base64_authorization_header.split(":")[1]
        return (username, userpwd)

    def user_object_from_credentials(self, user_email: str, user_pwd: str)\
            -> TypeVar('User'):
        """"get user object from db"""
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        if User.count() != 0:
            users = User.search({"email": user_email})
            if users:
                for user in users:
                    if not user.is_valid_password(user_pwd):
                        return None
                return user
            else:
                return None
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overload current user method"""
        if (self.authorization_header(request)) is not None:
            auth = self.extract_base64_authorization_header(
                request.headers.get('Authorization'))
            decoded_base64_str = self.decode_base64_authorization_header(auth)
            extracted_user = self.extract_user_credentials(decoded_base64_str)
            current_user = self.user_object_from_credentials(
                extracted_user[0], extracted_user[1])
            return current_user
