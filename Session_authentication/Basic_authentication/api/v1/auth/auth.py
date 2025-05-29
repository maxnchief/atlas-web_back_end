#!/usr/bin/env python3
"""
auth.py

This module defines the Auth class, which serves as a template for implementing
authentication systems in a Flask-based API. It provides methods to determine
if authentication is required for a given path, retrieve the authorization
header from a request, and obtain the current user associated with a request.

Classes:
    Auth: Template class for authentication logic.

Type Variables:
    User: Generic type variable representing a user object.

Methods:
    require_auth(path: str, excluded_paths: List[str]) -> bool:
        Determines if authentication is required for the specified path,
        based on a list of excluded paths.

    authorization_header(request=None) -> str:
        Retrieves the authorization header from the provided Flask request
        object, if present.

    current_user(request=None) -> User:
        Returns the current user associated with the request. This is a
        placeholder method to be implemented in subclasses.
"""
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """Template for authentication system."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns True if authentication is required for the given path.
        Returns True if path is None or excluded_paths is None or empty.
        Returns False if path matches any in excluded_paths (slash tolerant).
        """
        if path is None or not excluded_paths:
            return True
        # Ensure path ends with a slash for comparison
        if not path.endswith('/'):
            path += '/'
        for excluded in excluded_paths:
            if excluded == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the authorization header from the request."""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> User:
        """Returns the current user (None for now)."""
        return None
