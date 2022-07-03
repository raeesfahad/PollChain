from api.schema import Verification
from repositories.utils import Utils as helper
from database import connector
from database.models import Candydate, Voter
from database.models import User
from faker import Faker
from api.hashing import Hash
from repositories.security import manager

from fastapi import APIRouter, Depends, status, Response

router = APIRouter(
    prefix= '/api/system',
    tags=['System']
)
db = connector
fake = Faker()




@router.get('/insert_voters/',)
async def fill_voters(number):

    for i in range(0, int(number)):
        this_cnic = helper.get_random_digits(6) + helper.get_random_string(6)
        this_name = fake.name()
        this_address = fake.address()
        await db.insert(Voter(cnic = this_cnic, name = this_name, address = this_address, isValid = False, has_voted = False))

    return {"message" : f"{number} voter(s) are added"} 

@router.post('/insert_candiates')
async def insert_voters(can : Candydate):

    await db.insert(can)
    return f"{can.name} has been added"


@router.get('/all_candidates')

async def get_all():

    x_candidate = await db.get_candidates()
    return x_candidate

@router.post('/insert_voter')
async def insert_one_voter(request:Voter):

    object = await db.insert(Voter(cnic=request.cnic, public_key=request.public_key, name=request.name, address = request.address , isValid = False, has_voted = False ))
    return request

@router.post('/verify_voter', status_code=status.HTTP_200_OK)
async def verify_voter(request:Verification, response : Response):

    if (not request.private_key) or (request.cnic):
        data = await db.get_one(Voter, Voter.cnic == request.cnic)
        key_pair = helper.generate_keys()
        data.update(key_pair)
        await db.insert(data)
        response.status_code = status.HTTP_201_CREATED
        return {"message" : "You can now vote with your private key", "key_pair" : key_pair}
    
    if (not request.private_key) or (request.cnic):
        
        data = await db.get_one(Voter, Voter.private_key == request.private_key)
        
        if not data.has_voted:
            response.status_code = status.HTTP_204_NO_CONTENT
            return {"message" : "you have already voted"}
        
        response.status_code = status.HTTP_202_ACCEPTED
        return {"message" : "You are ready to vote"}
    
    if not request.cnic and request.private_key:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message" : "You are not eligible for voting"}


        





