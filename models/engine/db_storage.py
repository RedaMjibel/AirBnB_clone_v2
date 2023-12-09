#!/usr/bin/python3
"""This module defines the engine for the MySQL database"""

from models.base_model import BaseModel
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

user = os.getenv('HBNB_MYSQL_USER')
pwd = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')
env = os.getenv('HBNB_ENV')

class DBStorage:
    """Defining the class DBStorage"""

    __classes = [State, City, User, Place, Review, Amenity]
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for the class DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        '''
        query for all objects on the current database session
        '''
        classes = {
            "City": City,
            "State": State,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity,
        }
        result = {}
        query_rows = []

        if cls:
            '''Query for all objects belonging to cls'''
            if type(cls) is str:
                cls = eval(cls)
            query_rows = self.__session.query(cls)
            for obj in query_rows:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                result[key] = obj
            return result
        else:
            '''Query for all types of objects'''
            for name, value in classes.items():
                query_rows = self.__session.query(value)
                for obj in query_rows:
                    key = '{}.{}'.format(name, obj.id)
                    result[key] = obj
            return result
    
    def new(self, obj):
        """Method to add a new object to the current database"""
        DBStorage.__session.add(obj)

    def save(self):
        """Method to commit all changes to the current database"""
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """Method to delete a new object to the current database"""
        DBStorage.__session.delete(obj)

    def reload(self):
        """Method to create the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        DBStorage.__session = Session()

    def close(self):
        """Public method to call the remove method"""
        DBStorage.__session.close()

# Creating an instance of DBStorage and storing it in the variable storage
storage = DBStorage()
storage.reload()
