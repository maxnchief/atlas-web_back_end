from flask import request
from typing import List, TypeVar

User = TypeVar('User')

class Auth:
    """Template for authentication system."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if authentication is required for a given path."""
        return False

    def authorization_header(self, request=None) -> str:
        """Returns the authorization header from the request."""
        return None

    def current_user(self, request=None) -> User:
        """Returns the current user (None for now)."""
        return None