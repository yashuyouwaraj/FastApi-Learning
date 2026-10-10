from fastapi import FastAPI

app= FastAPI()

#Home route
@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "This is the about page"}

@app.get("/users")
def users():
    return {
    "users": [
            {"id": 1, "name": "John Doe"},
            {"id": 2, "name": "Jane Smith"},
            {"id": 3, "name": "Alice Johnson"}
        ]
    }
