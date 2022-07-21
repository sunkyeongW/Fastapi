from ast import Return
from ctypes import HRESULT
import enum
from typing import Optional, List
from unicodedata import name
from click import password_option
import uvicorn
from enum import Enum
from fastapi import FastAPI, status
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class CreateUser(BaseModel):
    name: str
    password: str
    avatar_url: HttpUrl = None

class GetUser(BaseModel): 
    name: str
    avatar_url:HttpUrl = "http://icotar.com/avatar/fastcampus.png?s=200"

class Item(BaseModel):
    name: str
    price : float
    amount = 0


class UserLeveL(str, Enum):
    a = "a"
    b = "b"
    c = "c"

class User(BaseModel):
    name: str
    password: str
    avatar_url: Optional[HttpUrl] = None
    inventory: List[Item] = []



@app.get("/")
def hello():
    return "Hello, Python!"

#response_model

#@app.post(
    #"/incloud",
    #response_model=CreateUser,
    #response_model_include={"name", "avatar_url"},
#)
#def get_user_with_include(user: CreateUser):
    #return user

#@app.post(
    #"/exclude",
    #response_model=CreateUser,
    #response_model_exclude={"password"},
#)    
#def get_user_with_exclude(user: CreateUser):
    #return user

#@app.post(
    #"/unset",
    #response_model=CreateUser,
    #response_model_exclude_unset=True,
#)
#def get_user_with_exclude_unset(user: CreateUser):
    #return user

@app.post("/post", response_model=GetUser, status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser):
    return user



@app.get("/grade")
def get_grade(grade: UserLeveL):
    return {"grade": grade}
    

@app.get("/users")
def get_users(is_admin:bool, limit:int = 100):
    return {"is_admin": is_admin, "limit": limit}

@app.get("/users/me", response_model=User)
def get_current_user():
    return {"user_my_id": 13}

@app.get("/users/item")
def get_users():
    fake_user = User(
        name="Fast",
        password="123",
        inventory=[
            Item(name="무기", price=1_000_000),
            Item(name="방어구", price=900_000),
        ]
    )
    return fake_user


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)