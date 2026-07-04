from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "Hello from main page"

@app.get("/about")
def about():
    return "Hello from about page"