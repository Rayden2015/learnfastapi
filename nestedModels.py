import uvicorn
from fastapi import FastAPI
from typing import Tuple
from pydantic import BaseModel

app = FastAPI()

class supplier(BaseModel):
    supplierID: int
    supplierName: str

class product(BaseModel):
    productID: int
    productName: str
    price: int
    supp: supplier

class customer(BaseModel):
    custID: int
    custname: str
    prod: Tuple[product]

@app.post("/invoice")
async def get_invoice(c1:customer):
        return c1
        