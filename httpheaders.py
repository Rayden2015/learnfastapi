import uvicorn
from fastapi import FastAPI, Header
from typing import Optional
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/headers/")
async def read_headers(accept_language: Optional[str] = Header(None)):
    return {"Accept-Language": accept_language}

@app.get("/rsheaders/")
def set_resp_headers():
    content = {"message": "Hellow Python - FAST API"}
    headers = {"X-Web-Framework": "FASTAPI", "Content-Language": "en-US"}
    return JSONResponse(content=content, headers=headers)
