from database import connector as db
from database.models import Voter as vt
from faker import Faker
from database.models import Candydate as can
from repositories.utils import Utils
import asyncio

async def main():
 fake = Faker()
 helper = Utils

 this_name = fake.name()
 this_party = input(str("Candidate Party: "))
 this_slogan = input(str("Slogan : "))

 instance = can(name = this_name, party = this_party, slogan=this_slogan)
 await db.insert(instance)
 print(f"Candidate {this_name} been inserted")