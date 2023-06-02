from fastapi import HTTPException
from fastapi import APIRouter

from ..database import User

from ..schemas import UserRequestModel
from ..schemas import UserResponseModel

router = APIRouter(prefix = '/api/v1/users')

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

