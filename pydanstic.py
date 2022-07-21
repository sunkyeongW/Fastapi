from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl






class User(BaseModel):
    name : str
    passwd : str
    avatar_url: Optional[HttpUrl] = None

app = FastAPI()

@app.post("/post")
def create_user(user: User):
    return user