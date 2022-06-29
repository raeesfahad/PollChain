from api import schema
from repositories.utils import Utils as helper
from database import connector
from database.models import Candydate, Voter
from database.models import User
from faker import Faker
from api.hashing import Hash
from repositories.security import manager

from fastapi import APIRouter, Depends

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