from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List

# Database setup with increased timeout
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False, "timeout": 30})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Database model
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publisher = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

# Pydantic models
class BookCreate(BaseModel):
    title: str
    author: str
    publisher: str

class BookUpdate(BaseModel):
    title: str
    author: str
    publisher: str

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    publisher: str

    class Config:
        orm_mode = True

# FastAPI app
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/add_new', response_model=BookResponse)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(title=book.title, author=book.author, publisher=book.publisher)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get('/books', response_model=List[BookResponse])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = db.query(Book).offset(skip).limit(limit).all()
    return books

@app.get('/books/{id}', response_model=BookResponse)
def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book

@app.put('/update/{id}', response_model=BookResponse)
def update_book(id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == id).first()
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    db_book.title = book.title
    db_book.author = book.author
    db_book.publisher = book.publisher
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete('/delete/{id}', response_model=dict)
def del_book(id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == id).first()
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    try:
        db.delete(db_book)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    return {"delete_status": "success"}

# To use MySQL or PostgreSQL, replace the SQLite engine with the appropriate one.
# Example:
# engine = create_engine('mysql+pymysql://user:password@localhost/test')
