from odmantic import ObjectId
from odmantic import AIOEngine


from database.models import Candydate, User, Voter, Chain

database = AIOEngine(database="Election_DB")



async def insert(instance):
    
    await database.save(instance)
  
    return print("[DB]:    Operation Completed (insert)")


async def insert_many(instance):

    await database.save_all()

    return print("[DB]:     Operation Completed (insert_many)")


async def get_one(instance, param):
    
    query = await database.find_one(instance, param)

    print("[DB]:   Operation Completed (get_one)") 

    return query


async def update_one(instance, param):

    query = await database.find_one(instance,param)

    return query



async def delete_all():

    users = await database.find(User)

    for _user in users:
       await database.delete(_user)


async def delete_one(id):

    user = await database.find_one(User, User.id == id)

    await database.delete(user)


async def update(id, object):


    user = await database.find_one(User, User.id == id)

    
    if object['name'] == "string" or "":
        object['name'] = user.name
    
    if object['email'] == "string" or "":
        object['email'] = user.email
    
    if object['password'] == "string" or "":
        object['password'] = user.password
    
    
    user.update(object)
    await database.save(user)

    return object



async def CheckVoter(cnic):

    voter = await database.find_one(Voter, Voter.cnic == cnic)

    if voter:
        return voter

    else:
        return {"message" : "User not in Voter lists"}


async def get_candidates():

    candidate = await database.find(Candydate)

    return candidate

async def Validator(instance,public_key,cnic):

    if public_key == null and cnic:
        
        param = await database.find(Instance, Voter.public_key == public_key)

    if not param.has_voted and param.isValid:
        return {"Message" : "You Have Already Voted"}
    else:
        return True

async def get_single_candidate(id): 

  uuid = ObjectId(id)

  candidate = await database.find_one(Candydate, Candydate.id == uuid)
  return candidate


async def get_db_chain():
    
    chain = await database.find_one(Chain)
    return chain