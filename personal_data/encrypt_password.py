#!/usr/bin/env python3
import bcrypt

def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt and returns the salted hash as bytes."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
