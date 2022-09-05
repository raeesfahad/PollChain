from datetime import datetime
from typing import Optional, List, Union

from odmantic import EmbeddedModel, Field, Model

class Candidate(EmbeddedModel):

    name : str
    party : str
    seat : str



class Voter(Model):
    cnic : str
    name : str
    address : str
    has_voted : bool = False
    private_key : Optional[str]

class User(Model):
    picture : str
    name : str
    email : str
    password : str

class Vote(Model):
    candidate : Candidate

class Chain(Model):
    instance : List

class Candydate(Model):
    name : str
    party : str
    slogan : str
    image : str




