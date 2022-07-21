from fastapi import FastAPI, Cookie
import fastapi

app = FastAPI()

@app.get("/cookie")
def get_cookie(ga: str = Cookie(None)):
    return {"ga":ga}

    
