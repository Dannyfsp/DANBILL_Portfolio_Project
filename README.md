# DANBILL
## Background Context
An e-commerce portfolio project given by ALX.
This project comprises of both Frontend and Backend and latest technologies above all.
### Authors
- Aghogho Daniel Bogare
- Bill Otieno

## Classes
#### User
A class representing a user with the following attributes:
- id
- firstName
- lastName
- email
it also contains the following methods 
- to_dict(): Returns the user's attributes as a dictionary.
- password: Property representing the hashed password.
- password.setter: Setter for the hashed password.
- checkPassword(password): Checks if the hashed password matches the provided password.
- __repr__(): Returns a string representation of the user.

### Product
A class representing a product with the following attributes:

- id: Integer (primary key)
- name: String
- description: String
- price: Float
- priceAfter: Float
- reviews: Integer
- ratings: Float

It also contains the following methods:

- to_dict(): Returns the product's attributes as a dictionary.
- __repr__(): Returns a string representation of the product.

### Category
A class representing a category with the following attributes:

- id: Integer (primary key)
- name: String
It also contains the following methods:

- to_dict(): Returns the category's attributes as a dictionary.
- __repr__(): Returns a string representation of the category.

### Usage
To use this script, you will need to have SQLAlchemy, Flask-Login, and Werkzeug installed. Once you have those dependencies installed, you can create instances of the User, Product, and Category classes and store them in a database using SQLAlchemy.

 ***console.py usage***
- set the environment variable my running the environ.sh `./environ.sh`
- confirm the environment variables have the correct values by running the environ.py `./environ.py`
- to get the deatils of a user if you have the user class and id run the console.py `./console.py` then type `show User 1` where 1 is the id of the user
- to create a user `./console.py` then type `create User name="user" email="user@app"` this creates a user with the given attributes
 