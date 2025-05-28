#!/usr/bin/env python3
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt and returns the salted hash as bytes."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if the provided password matches the hashed password using bcrypt."""
    return bcrypt.checkpw(password.encode(), hashed_password)
