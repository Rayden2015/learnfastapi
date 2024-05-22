from fastapi import FastAPI, Cookie
from fastapi.responses import JSONResponse
import uuid

app = FastAPI()

@app.post("/cookie/")
def create_cookie():
    content = {"message": "cookie set"}
    response = JSONResponse(content=content)
    uuid = uuid.uuid
    response.set_cookie(key="username", value=uuid)
    return response

@app.get("/readcookie")
async def read_cookie(username:str=Cookie(None)):
    return {"username": username}

