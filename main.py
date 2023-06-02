from fastapi import FastAPI
from fastapi import HTTPException

from database import User
from database import Movie
from database import UserReview

from database import database as connection

from schemas import UserRequestModel
from schemas import UserResponseModel

#Start the server: uvicorn main:app

app = FastAPI(title = 'Project Movie Review',
            description = 'In this project we create a web app to share movie reviews',
            version = '1')

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User, Movie, UserReview])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()



@app.get('/')
async def index():
    return 'Hello world from fastAPI server'

@app.post('/users', response_model = UserResponseModel)
async def create_user(user: UserRequestModel):
    
    if User.select().where(User.username == user.username).exists():
        return HTTPException(409, 'The username is already in use')

    hash_password = User.create_password(user.password)

    user = User.create(
         username = user.username,
         password = hash_password 
    )

    return UserResponseModel(id = user.id, username = user.username)