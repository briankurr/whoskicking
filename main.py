from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    response = {"Hello,": "World!"}
    return response