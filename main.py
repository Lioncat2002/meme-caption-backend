import os
import io
import base64
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/")
def read_root():
    return {"This is": "a test"}


@app.post("/upload/")
async def upload(file:bytes=File()):#: bytes = File()):
    # TODO: Pass the base64 file to the ml model
    with open("tmp/test.png", "wb") as fo:
        fo.write(file)
    return {"file": "file uploaded"}
    # contents = file.file.read()
    # if not file.filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
    #    return {"error": "File is not an image"}
    ## TODO: Add a function call here to the ML model which will accept the file object
    # f = io.TextIOWrapper(
    #    file.file
    # )  # to convert the UploadFile into a python file object
    ## temporary code to write image on to the disk
    # if not os.path.exists("tmp"):
    #    os.makedirs("tmp")
    # with open("tmp/img.jpeg", "wb") as f:
    #    f.write(contents)

    #    return {"filename": file.filename}
    # Possibly make it so that this single endpoint returns caption?
