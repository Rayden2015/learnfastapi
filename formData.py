import uvicorn
from fastapi import Form, FastAPI,File, UploadFile, Request
from pydantic import BaseModel
import shutil
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import uuid
templates = Jinja2Templates(directory="templates")



app = FastAPI()

# @app.post("/submit/")
# async def submit(nm: str = Form(...), pwd: str = Form(...)):
#     return {"username": nm, "password":pwd}

class User(BaseModel):
    username: str
    password: str

@app.post("/submit/", response_model=User)
async def submit(nm: str = Form(...), pwd: str = Form(...)):
    return User(username=nm, password=pwd)


@app.get("/upload/", response_class=HTMLResponse)
async def upload(request: Request):
     return templates.TemplateResponse("uploadfile.html", {"request": request})


@app.post("/uploader")
async def create_upload_file(file: UploadFile = File(...)):
    # Generate a unique filename (optional)
    filename = f"{uuid.uuid4()}.png"
    
    # Ensure write permissions (adjust path as needed)
    filepath = "uploads/"+filename
    os.makedirs(os.path.dirname(filepath), exist_ok=True)  # Create directory if it doesn't exist
    
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}
