#!/usr/bin/env python3

"""This module defines the BasicAuth class, which implements HTTP Basic
Authentication for the API. It provides methods to extract and decode
credentials from the Authorization header, and to validate user credentials.

BasicAuth: Inherits from Auth and implements methods for handling
Basic Authentication.

Methods:
extract_base64_authorization_header(authorization_header: str) -> str:
    Extracts the Base64 part of the Authorization header if present.

decode_base64_authorization_header(base64_authorization_header: str) -> str:
    Decodes a Base64-encoded string and returns its UTF-8 representation.

extract_user_credentials(decoded_base64_authorization_header: str) -> (str, str):
    Splits the decoded string into user email and password.

user_object_from_credentials(user_email: str, user_pwd: str) -> TypeVar('User'):
    Returns a User instance if the email and password are valid.

Use the BasicAuth class as part of the API authentication system to
validate user credentials provided via HTTP Basic Authentication.

basic_auth.py

This module defines the BasicAuth class, which provides a basic authentication mechanism
for the API. It inherits from the Auth base class and is intended to implement methods
for handling HTTP Basic Authentication.

Classes:
    BasicAuth: A subclass of Auth that will implement basic authentication logic.

Usage:
    This module is intended to be used as part of the authentication system for the API.
    Extend the BasicAuth class to implement methods for extracting and validating user
    credentials from HTTP requests.

Example:

    basic_auth = BasicAuth()
    # Use basic_auth methods to authenticate requests

"""
from api.v1.auth.auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth."""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization header for Basic Authentication.
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ", 1)[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Returns the decoded value of a Base64 string base64_authorization_header.
        """
        import base64
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None or not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            from models.user import User
            users = User.search({"email": user_email})
            if not users or len(users) == 0:
                return None
            user = users[0]
            if not user.is_valid_password(user_pwd):
                return None
            return user
        except Exception:
            return None
