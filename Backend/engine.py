from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models import User, Category, Product, Base


class Engine:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
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

"""# Define the database URL
db_url = "mysql://<user>:<password>@<host>/<database_name>"

# Create the database engine
engine = create_engine(db_url)

# Create a session factory
Session = sessionmaker(bind=engine)


# Create the tables in the database
Base.metadata.create_all(bind=engine)

# Create a session
session = Session()

# Add a new user
user = User(firstName="John", lastName="Doe", email="johndoe@example.com")
session.add(user)
session.commit()

# Add a new category
category = Category(name="Books")
session.add(category)
session.commit()

# Add a new product with a category
product = Product(name="Book Title", description="Book Description", price=9.99, priceAfter=8.99, reviews=0, ratings=0)
product.categories.append(category)
session.add(product)
session.commit()

# Query the database
users = session.query(User).all()
print(users)

products = session.query(Product).all()
print(products)

categories = session.query(Category).all()
print(categories)

# Close the session
session.close()
"""