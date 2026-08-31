from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def home():
    return "this is home page"

@app.get("/login")
def login():
    return "this is login page"

@app.get("/signup")
def signup():
    return "this is signup page"

@app.get("/dashboard")
def dashbaord():
    return "this is dashbaord page"
