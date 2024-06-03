from fastapi import FastAPI

app = FastAPI()

@app.get("/app")
def mainindex():
    return {"message": "Hello World from TOp Level App"}


subapp = FastAPI()

@subapp.get("/sub")
def subindex():
    return {"message": "Hello World from TOp Level Sub"}

app.mount("/subapp", subapp)
