#!/usr/bin/env python3
""" A Module to hash and validate passwords with bcrypt """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashes a password with a random salt using bcrypt. """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates the given password against a hashed password """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
