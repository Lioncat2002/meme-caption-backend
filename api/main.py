from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/")
def read_root():
    return {"This is": "a test"}


@app.post("/upload/")
async def upload(file: UploadFile):
    contents = await file.read()  # --> file is a standard python file object
    # TODO: Add a function call here to the ML model which will accept the file object

    # temporary code to write image on to the disk
    with open("tmp/img.jpeg", "wb") as f:
        f.write(contents)
    return {
        "filename": file.filename
    }  # Possibly make it so that this single endpoint returns caption?
