from pymongo import MongoClient
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List
import os

app = FastAPI()

# Define the database and collection names
DB_NAME = "FastDB"
BOOK_COLLECTION = "books"

# MongoDB connection settings
MONGO_USERNAME = "nurundin2010"
MONGO_PASSWORD = "TK7rEzfKovE191Y7"
MONGO_HOST = "estdb.pjrvppo.mongodb.net/?retryWrites=true&w=majority&appName=TestDB"  # e.g., "localhost" or the MongoDB server's IP address
MONGO_PORT = "27017"  # e.g., "27017" (default MongoDB port)

#mongodb+srv://nurundin2010:<password>@testdb.pjrvppo.mongodb.net/?retryWrites=true&w=majority&appName=TestDB

# Construct the MongoDB connection URI
#MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"


class Book(BaseModel):
    bookID: int
    title: str
    author: str
    publisher: str

@app.post("/add_new", status_code=status.HTTP_201_CREATED)
def add_book(b1: Book):
    """Post a new book to the specified collection."""
    try:
        with MongoClient(MONGO_URI) as client:
            book_collection = client[DB_NAME][BOOK_COLLECTION]
            result = book_collection.insert_one(b1.dict())
            ack = result.acknowledged
            return {"insertion": ack}
    except Exception as e:
        return {"error": str(e)}

# To run the app, use: uvicorn script_name:app --reload

@app.get("/books", response_model=List[str])
def get_books(MONGO_URI):
    """Get all books in list form."""
    with MongoClient() as client:
        book_collection = client[DB_NAME][BOOK_COLLECTION]
        booklist = book_collection.distinct("title")
        return booklist


@app.get("/books/{id}", response_model=Book)
def get_book(id: int):
    """Get all messages for the specified channel."""
    with MongoClient(MONGO_URI) as client:
        book_collection = client[DB_NAME][BOOK_COLLECTION]
        b1 = book_collection.find_one({"bookID": id})
        return b1

