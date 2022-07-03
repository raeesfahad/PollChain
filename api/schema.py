from pydantic import BaseModel
from repositories import utils
from database.models import Candidate
from typing import Optional


class vote(BaseModel):
    public_key : str
    candidate : Candidate


class User(BaseModel):

    name : str 
    email : str
    password : str

class Verification(BaseModel):
    private_key : Optional[str]
    cnic : Optional[str]