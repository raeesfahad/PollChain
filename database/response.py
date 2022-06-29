
from odmantic import Model
from .models import User
from odmantic.bson import ObjectId


class User(Model):
    email : str
    name : str