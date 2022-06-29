from fastapi_login import LoginManager
from odmantic import ObjectId
from database.models import User
from database import connector as db


secret_key = "c3cad00035c13e7a6bfaaa4abf17e3fa6a5bd5b788c9e0a2"

manager = LoginManager( secret_key, '/login')


@manager.user_loader()
async def users_get_single(email:str):



    user = await db.get_one(User, User.email == email)

    return user