#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
import logging

from user import Base

logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str):
        """Add a new user to the database and return the User object."""
        from user import User
        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def find_user_by(self, **kwargs):
        """Finds a user by arbitrary keyword arguments."""
        from user import User
        session = self._session
        user = session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound()
        return user
