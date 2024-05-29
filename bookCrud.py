from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

data = []
i = 0

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str

@app.post("/book")
def add_book(book: Book):
    global i
    i += 1
    book.id = i
    data.append(book.dict())
    return {"message": "Book added successfully", "book": book}

@app.get("/books", response_model=List[Book])
def get_books():
    return data


@app.get("/book/{id}")
def get_book(id: int):
    id = id - 1
    return data[id]


@app.put("/book/{id}")
def add_book(id: int, book: Book):
    data[id-1] = book
    return data

@app.delete("/book/{id}")
def delete_book(id: int):
    data.pop(id-1)
    return data