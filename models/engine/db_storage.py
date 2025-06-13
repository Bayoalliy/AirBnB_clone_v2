#!/usr/bin/python3
"""
This module manages our database storage.
a class is created in this respect.
"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base


class DBStorage():
    """database storage class definition"""

    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity

        dic = {}

        if cls:
            if type(cls) == str:
                cls = eval(cls)
            query = self.__session.query(cls).all()
            for elem in query:
                dic['{}.{}'.format(elem.__class__.__name__, elem.id)] = elem

        else:
            lst = [State, City, User, Place, Review, Amenity]
            for clas in lst:
                query = self.__session.query(clas).all()
                for elem in query:
                    dic['{}.{}'.format(type(elem).__name__, elem.id)] = elem
        return dic

    def new(self, obj):
        """adds tge obj to current database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Sess)
        self.__session = Session()

    def close(self):
        """Closes a session"""
        self.__session.close()
