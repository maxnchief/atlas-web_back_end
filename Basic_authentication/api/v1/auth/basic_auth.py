#!/usr/bin/env python3
"""
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
