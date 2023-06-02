from typing import Any

from pydantic import BaseModel
from pydantic import validator

from peewee import ModelSelect


"""class PeeweGetterDict(dict):
    def get(self, key:Any, default: Any = None):     #Convert our model object to a dict
        
        res = getattr(self.obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)

        return res"""

class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls, username):
        if len(username) < 3 or len(username) > 50:
            raise ValueError('Length must be between 3 and 50 characters')

        return username


class UserResponseModel(BaseModel):
    id : int 
    username : str

    """class Config:
         orm_mode = True
         getter_dict = PeeweGetterDict"""

# ---------------- Movie --------------------

"""class MovieResponseModel(BaseModel):
    id: int
    title: str"""



# ---------------- Review --------------------

class Review_validator():
    @validator('score')
    def score_validator(cls, score):
        if score < 0 or score > 5:
            raise ValueError('The score range is from 0 to 5')

        return score

class ReviewRequestModel(BaseModel, Review_validator):
    user_id: int
    movie_id: int
    review: str
    score: int

class ReviewResponseModel(BaseModel):
    id: int
    movie_id: int   #MovieResponseModel to relationed models
    review: str
    score: int

class ReviewRequestPutModel(BaseModel, Review_validator):
    review: str
    score: int


