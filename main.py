from ast import Return
from ctypes import HRESULT
import enum
from typing import Optional, List
from unicodedata import name
from urllib import response
from click import password_option
import uvicorn
from enum import Enum
from fastapi import FastAPI, status, Query, Path, Cookie, Header
from pydantic import BaseModel, HttpUrl, parse_obj_as, Field
from typing import List

app = FastAPI()


inventory = (
    {
        "id" : 1,
        "user_id" : 1,
        "name": "포션",
        "price": 2500.0,
        "amount" : 100,
    },
    {
        "id" : 2,
        "user_id" : 1,
        "name": "won",
        "price": 500.0,
        "amount" : 50,
    },
)


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

class Item2(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, title="이름")
    price: float = Field(None, ge=0)
    amount: int = Field(
        default=1,
        gt=0,
        le=100,
        title="수량",
        description="아이템 갯수. 1~100개 까지 소지 가능"
    )


class UserLeveL(str, Enum):
    a = "a"
    b = "b"
    c = "c"

class User(BaseModel):
    name: str
    password: str
    avatar_url: Optional[HttpUrl] = None
    inventory: List[Item] = []

@app.get("/header")
def get_headers(x_token: str = Header(None, title="토큰")):
    return {"X-Token": x_token}


@app.get("/cookie")
def get_cookie(ga: str = Cookie(None)):
    return {"ga": ga}

@app.get("/user/{user_id}/item")
def create_item(item: Item2):
    return item


@app.get("/user/{user_id}/inventory", response_model=List[Item])
def get_item(
    user_id: int = Path(..., gt=0, title="사용자 ID", description="DB의 user.id"),
    name: str = Query(None, min_length=1, max_length=3, title="아이템 이름"),
):
    user_items = []
    for item in inventory:
        if item["user_id"] == user_id:
            user_items.append(item)

    response = []
    for item in user_items:
        if name is None:
            response = user_items
            break
        if item["name"] == name:
            response.append(item)
    return response


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