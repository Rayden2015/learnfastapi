import uvicorn
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

class User:
    def __init__(self, id: str, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age

def validate_user(user: User = Depends(User)):
    if user.age < 18:
        raise HTTPException(status_code=400, detail="You are not Eligible")
    return user

@app.get("/user/")
async def get_user(user: User = Depends(validate_user)):
    return user


async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
    

@app.get("/admin/")
async def get_admin(user: User = Depends(validate_user)):
    # Implement admin-specific logic here (e.g., authorization checks)
    get_db()
    return {"message": "Welcome, Admin!"}

