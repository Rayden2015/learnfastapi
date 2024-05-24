import unvicorn
from fastapi import FastAPI

app= FastAPI()

async def dependency(id:str, name: str, age:int):
    return {"id":id, "name":name, "age":age}

class dependency:
    def __init__(self, id:str, name:str, age:int):
        self.id = id
        self.name = name
        self.age = age

@app.get("/user/")
async def user(dep:dependency = Depends(dependency)):
    return dep

@app.get("/admin/")
async def admin(dep:dependency = Depends(dependency)):
    return dep

