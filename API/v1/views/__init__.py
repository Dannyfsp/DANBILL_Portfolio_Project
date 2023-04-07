"""we setup the app blueprint """
from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
from API.v1.views.users import *
