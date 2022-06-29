from pydantic import BaseModel
from repositories import utils
from database.models import Candidate


class vote(BaseModel):
    public_key : str
    candidate : Candidate


class User(BaseModel):

    name : str 
    email : str
    password : str