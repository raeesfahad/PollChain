from routes import users, blockhain_r, system
from repositories.utils import Utils as helper
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(blockhain_r.router)
app.include_router(system.router)


app.mount("/", StaticFiles(directory="static/", html=True), name="static")

    

