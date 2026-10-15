from fastapi import FastAPI
app = FastAPI(title="lahari")

@app.get("/")
def home():
    return {"message" : "Hi fastapi"}

@app.get("/name")
def name():
    return {"batch - 576"}