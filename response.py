from typing import Optional

from fastapi import FastAPI
from pydanstic import BaseModel, HttpUrl

app = FastAPI()

class User(BaseModel):
    name: str
    password: str
    avatar_url: Optional[HttpUrl] = None


class CreateUser(BaseModel):
    name: str
    password: str
    avatar_url: HttpUrl = "https://icotar.com/avatar/fastcampus.png?s=200"

class GetUser(BaseModel):
    name: str
    avatar_url: HttpUrl = "https://icotar.com/avatar/fastcampus.png?s=200"
    

@app.get("/users/me", response_model=GetUser) #응답모델
def create_user(user: CreateUser):   #요청 모델
    return user