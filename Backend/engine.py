
#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


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
        from Backend.models import Base
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
    
    def all(self, obj=None):
        """we get all the objects in the database"""
        from Backend.models import User, Category, Product
        classdic = { "User": User, "Category":Category, "Product":Product}
        objdict = {}
        for cls in classdic:
            if obj is None or obj is classdic[cls] or cls is obj:
                objs = self.__session.query(classdic[cls]).all()
                for ob in objs:
                    key = ob.__class__.__name__ + "." + str(ob.id)
                    objdict[key] = ob
        return objdict
    
    def get(self, cls, id):
        """ we retrive a particular class from the database"""
        from Backend.models import User, Category, Product
        from Backend import Storage
        classdic = { "User": User, "Category":Category, "Product":Product}
        if cls not in classdic.values():
            return None
        classes = Storage.all(cls)
        for clas in classes.values():
            if clas.id == int(id):
                return clas
        return None


    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
