#!/usr/bin/python3
"""we set up the api endpoints for the user"""
from flask import jsonify, abort, make_response, request
from Backend import Storage
from Backend.models import User
from API.v1.views import app_views

@app_views.route('/users', methods=['GET'],
                  strict_slashes=False)
def getAlluser():
    """we get all users"""
    userlist = []
    alluser = Storage.all(User)
    for obj in alluser.values():
        userlist.append(obj.to_dict())
    return jsonify(userlist)

@app_views.route('/users/<user_id>', methods=['GET'],
                  strict_slashes=False)
def getuser(user_id):
    """we get a user by id"""
    user = Storage.get(User, user_id)
    if user:
        return jsonify(user.to_dict())
    else:
        abort(404)

@app_views.route('/users/<user_id>', methods=['DELETE'],
                  strict_slashes=False)
def delUser(user_id):
    """ delete a user based on the id """
    user = Storage.get(User, user_id)
    if user:
        Storage.delete(user)
        Storage.save()
        return make_response(jsonify({}), 200)
    else:
        abort(404)

@app_views.route('/users', methods=['POST'],
                  strict_slashes=False)
def postUser():
    """ adds a user """
    post = request.get_json()
    if not post:
        abort(400, description="Not a Json")
    if "name" not in post:
        abort(400, description="Missing Name")
    if "email" not in post:
        abort(400, description="Missing Email")
    instance = User(**post)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/users/<user_id>', methods=['PUT'],
                 strict_slashes=False)
def updateUser(user_id):
    """updates the user"""
    user = Storage.get(User, user_id)
    put = request.get_json()
    if not user:
        abort(404)
    if not put:
        abort(400, description="Not a Json")
    ignore = ["email", "id"]
    for k, v in put.items():
        if k not in ignore:
            setattr(user, k, v)
    Storage.save()
    return make_response(jsonify(user.to_dict()), 200)
