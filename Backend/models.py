""""This script contains all the ensentail user info"""

from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declarative_base
from engine import mstorage
Base = declarative_base()

productCategory = Table("productCategory", Base.metadata, 
                        Column("productId", Integer, ForeignKey("products.id")),
                        Column("CategotyId", Integer, ForeignKey("categories.id")))
def Save(self):
    """ we impliment a funtion"""
    storage.reload()
    storage.new(self)
    stotage.save()

class User(UserMixin, Base):
    """This class contains all the relevant info of a user"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    firstName =Column(String(256), nullable=False)
    lastName = Column(String(256), nullable=False)
    email = Column(String(256), unique=True, nullable=False)

    def to_dict(self):
        """We create a dict with the class attributes as values"""
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email
        }
    
    @property
    def password(self):
        """We access the password method as an attribute"""
        return self.hashedPassword
    
    @password.setter
    def password(self, password):
        """we set the value of hashedPasword"""
        self.hashedPassword = generate_password_hash(password)
    
    def checkPassword(self, password):
        """We check if the hashed password matches"""
        return check_password_hash(self.password, password)

    def __repr__(self):
        """We get the  class attributes as strings"""
        return f"ID: {self.id} \nFirstName: {self.firstName} \nEmail: {self.email}"
    def save(self):
        """saves the instance"""
        Save()
    
class Product(Base):
    """this is a class containing products"""
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
    description = Column(String(256), nullable=False)
    price = Column(Float, nullable=False)
    priceAfter = Column(Float, nullable=False)
    reviews = Column(Integer)
    ratings = Column(Float)
    categories = relationship("Category", secondary="productCategory", backref = "products")

    def to_dict(self):
        """We get the class in a dictionary"""
        return {
            "id" : self.id,
            "name" : self.name,
            "description" : self.description,
            "price" : self.price,
            "priceAfter" : self.priceAfter,
            "reviews" : self.reviews,
            "ratings" : self.ratings
        }

    def __repr__(self) -> str:
        return f"ID: {self.id} \nName: {self.name} \nDescption: {self.description} \nPrice: {self.price}"

    def save(self):
        """saves the instance"""
        Save()
    
class Category(Base):
    """This is a class with all categories relatable stuff"""
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable= False)

    def to_dict(self):
        """Representing the class as dict"""
        return {
            "id" : self.id,
            "name" : self.name
        }
    
    def __repr__(self) -> str:
        return f"ID: {self.id} \nName: {self.name}"

    def save(self):
        """saves the instance"""
        Save()