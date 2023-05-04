#!/usr/bin/env python3
"""Basic authentication module"""


from api.v1.auth.auth import Auth
import base64
from typing import Tuple


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
