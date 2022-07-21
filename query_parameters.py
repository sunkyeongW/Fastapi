from enum import Enum
import uvicorn

from fastapi import FastAPI

app = FastAPI()

class UserLevel(str,Enum):
    a = "a"
    b = "b"
    c = "c"

@app.get("/grade")
def get_grade(grade: UserLevel):
    return {"grade": grade}

@app.get("/users")
def get_users(is_admin: bool, limit: int = None):
    return {"is_adim": is_admin ,"limit": limit}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)