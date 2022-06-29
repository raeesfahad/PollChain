from asyncore import file_dispatcher
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from odmantic import ObjectId
from api.hashing import Hash
from database.models import User
from database import connector as db
from repositories.security import manager
from database.connector import database
from fastapi import status as http_rc
from fastapi import File, UploadFile



router = APIRouter(
    prefix= '/api/users',
    tags=['Users']
)

@router.post('/login')

async def login( data: OAuth2PasswordRequestForm = Depends()):

    email = data.username
    password = data.password


    user = await db.get_one(User, User.email == email)

    if not user:

        raise InvalidCredentialsException
    
    elif password != user.password:

        raise InvalidCredentialsException
    
    access_token = manager.create_access_token(
        data={'sub': email}
    )
    return {'access_token': access_token}




@router.post('/add', status_code=http_rc.HTTP_201_CREATED)
async def users_add_single(request:User):

    #hashed_pass = Hash.HashPassword(request.password)
    
    checklist = [ "string", "", " "]


    if request.email or request.name or request.password in checklist:
        return {"message" : "Blank values cant be stored"}

    user_obj = await db.get_one(User, User.email == request.email) 


    if user_obj != None and user_obj.email == request.email:
        return { "error": "User already exists"}

    if user_obj is None:
        await db.insert(User(name = request.name, email = request.email, password=request.password))
        return {"message" : "successfully added user"}


@router.get('/{id}')
async def users_get_single(id):

    uuid = ObjectId(id)

    user = await db.get_one(User, User.id == uuid)

    return user



@router.delete('/delete/{id}')
async def users_delete_one(id):

    uuid = ObjectId(id)

    await db.delete_one(uuid)


    return {"message" : "user deleted successfully"}

    
@router.delete('/delete/all')
async def users_delete_all():


     user = await db.delete_all()

     return {"message" : f"all users have been deleted"}


@router.put('/update/{id}', status_code=http_rc.HTTP_201_CREATED)

async def users_update(id, request:User):

    uuid = ObjectId(id)

    edited_user = {"name" : request.name, "email": request.email, "password" : request.password}

    await db.update(uuid, edited_user)

    return {"message" : "success"}




