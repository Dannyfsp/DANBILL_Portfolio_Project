#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models import User, Category, Product, Base


class storage():
    __engine = None
    __session = None
    def __init__(self):
        # Define the database URL
        APP_MYSQL_USER = getenv('APP_MYSQL_USER')
        APP_MYSQL_PWD = getenv('APP_MYSQL_PWD')
        APP_MYSQL_HOST = getenv('APP_MYSQL_HOST')
        APP_MYSQL_DB = getenv('APP_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                    format(APP_MYSQL_USER,
                                            APP_MYSQL_PWD,
                                            APP_MYSQL_HOST,
                                            APP_MYSQL_DB))
        
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
