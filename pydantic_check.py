from typing import List
from pydantic import BaseModel, Field

# class Student(BaseModel):
#     id: int
#     name: str
#     subjects: List[str] =[]

class Student(BaseModel):
    id: int
    name: str = Field(None, title="The description of the item", max_length=10)
    subjects: List[str] = []

data = {
'id': 1,
'name': 'Ravikumar',
'subjects': ["Eng", "Maths", "Sci"],
}

s1= Student(**data)

print(s1)

s1.dict()


data = {
'id': [1,2],
'name': 'Ravikumar Singhest',
'subjects': ["Eng", "Maths", "Sci"],
}

s2= Student(**data)

print(s2)

