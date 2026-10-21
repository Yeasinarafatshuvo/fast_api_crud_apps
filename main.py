from fastapi import FastAPI

from app.routes import employee_router

app = FastAPI(title="Employee Management API")

app.include_router(employee_router)


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


@app.get("/about")
def about():
    return {
        "name": "Yeasin",
        "role": "Python Developer",
    }