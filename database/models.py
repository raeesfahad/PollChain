from datetime import datetime
import string
from typing import Optional, List

from odmantic import EmbeddedModel, Field, Model

class Candidate(EmbeddedModel):

    name : str
    party : str
    seat : str



class Voter(Model):
    cnic : str
    name : str
    address : str
    isValid : bool = False
    has_voted : bool = False

class User(Model):
    picture : str
    name : str
    email : str
    password : str

class Vote(Model):
    public_key : str
    candidate : Candidate

class Chain(Model):
    instance : List

class Candydate(Model):
    name : str
    party : str
    slogan : str
    image : str




