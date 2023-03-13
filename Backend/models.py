""""This script contains all the ensentail user info"""

from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
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