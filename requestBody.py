import uvicorn
from fastapi import FastAPI, Body
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()

# Using BaseModel as Request Body Validation
class Student(BaseModel):
    id: int
    name: str = Field(None, title="name of student", max_length=10)
    subjects: List[str] = []


# @app.post("/students/")
# async def student_data(s1: Student):
#     return s1

#using Body from fastapi as RequestBody Validation
@app.post("/students")
async def student_data(name: str=Body(...),
marks:int=Body(...)):
    return {"name": name, "marks": marks}

@app.post("/students/{college}")
async def student_data(college:str, age: int, student: Student):
    retval={"college": college, "age": age, **student.dict()}
    return retval