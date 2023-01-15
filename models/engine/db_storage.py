#!/usr/bin/python3
""" dbstorage enggine """
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """ data base storage engine """

    __engine = None
    __session = None

    def __init__(self):

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of objects form database
        """
        objs_list = []
        if cls is None:
            all_cls = [City, State]
            for obj in all_cls:
                objs_list.extend(self.__session.query(obj).all())
        else:
            if isinstance(cls, str):
                cls = classes[cls]
            elif cls not in classes.values():
                return
            objs_list = self.__session.query(cls).all()

        objs_dict = {"{}.{}".format(v.__class__.__name__,
                                    v.id): v for v in objs_list}
        return objs_dict

    def new(self, obj):
        """Adds new object to the table"""
        self.__session.add(obj)

    def save(self):
        """ commit all the changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current databsae session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Load for database """
        Base.metadata.create_all(self.__engine)
        scoop = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(scoop)

    def close(self):
        """ method to retrive from the db storage """
        self.__session.remove()
