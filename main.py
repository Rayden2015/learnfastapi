import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def sayhello(name: str):
     a =  "Hello " + " " + name.swapcase()
     return {"name": a}


@app.get("/hello/{name}/{age}")
async def age(name:str,age:int):
    return{"name": name, "age": age}



if __name__ == "__main__":
     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
