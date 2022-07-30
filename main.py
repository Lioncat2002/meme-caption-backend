import os
import io
import tempfile
import base64
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ImageData(BaseModel):
    data:str


@app.get("/")
def read_root():
    return {"This is": "a test"}

@app.post("/encoded/")
async def base64data(data:ImageData):
    print("Success")
    d=base64.b64decode(data.data.encode('utf-8'))
    f=io.BytesIO(d)
    f=Image.open(f) #PIL image
    #f.show()
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    with open("tmp/t.png","wb") as fs:
        fs.write(d)
    #f=io.BytesIO(data)
    return {"got":"ze file"}

    

@app.post("/image/")
async def imageupload(data:UploadFile=File(...)):
    print("Success")
    f=data.file
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    with open("tmp/image.jpg","wb") as fs:
        fs.write(f.read())
    f=Image.open(f)
    f.show()
    return {"got":"success"}

@app.post("/upload/")
async def upload(file:bytes=File()):#: bytes = File()):
    # TODO: Pass the base64 file to the ml model
    #with open("tmp/test.png", "wb") as fo:
    #    fo.write(file)
    #return {"file": "file uploaded"}
     contents = file
     #if not file.filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
     #   return {"error": "File is not an image"}
    # TODO: Add a function call here to the ML model which will accept the file object
     
    # temporary code to write image on to the disk
     if not os.path.exists("tmp"):
        os.makedirs("tmp")
     with open("tmp/img.jpeg", "wb") as f:
        f.write(contents)

     return {"file": "uploaded"}
    # Possibly make it so that this single endpoint returns caption?
