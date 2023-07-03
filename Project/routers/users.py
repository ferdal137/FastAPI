from typing import List

from fastapi import Cookie
from fastapi import Response

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends

from fastapi.security import HTTPBasicCredentials

from ..database import User

from ..common import oauth2_schema

from ..schemas import UserRequestModel
from ..schemas import UserResponseModel
from ..schemas import ReviewResponseModel

router = APIRouter(prefix = '/users')

@router.post('', response_model = UserResponseModel)
async def create_user(user: UserRequestModel):
    
    if User.select().where(User.username == user.username).exists():
        return HTTPException(409, 'The username is already in use')

    hash_password = User.create_password(user.password)

    user = User.create(
         username = user.username,
         password = hash_password 
    )

    #return user
    return UserResponseModel(id = user.id, username = user.username)

@router.post('/login', response_model = UserResponseModel)
async def login(credentials: HTTPBasicCredentials, response: Response):
    
    user = User.select().where(User.username == credentials.username).first()

    if user is None:
        raise HTTPException(404, 'User not found')

    if user.password != User.create_password(credentials.password):
        raise HTTPException(404, 'Password error')

    response.set_cookie(key='user_id', value = user.id)
    return UserResponseModel(id = user.id, username = user.username)

"""
@router.get('/reviews', response_model = List[ReviewResponseModel])
async def get_reviews(user_id: int = Cookie(None)):
    
    user = User.select().where(User.id == user_id).first()

    if user is None:
        raise HTTPException(404, 'User not found')

    return [ user_review for user_review in user.reviews ]"""


@router.get('/reviews')
async def get_reviews(token: str = Depends(oauth2_schema)):
    return {


    }