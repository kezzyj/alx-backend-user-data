#!/usr/bin/env python3
"""a module to manage the API authentication
"""

from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """SessionAuth class"""
    pass
