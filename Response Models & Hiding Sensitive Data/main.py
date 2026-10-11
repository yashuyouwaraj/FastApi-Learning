from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id:int
    name:str
    age:int
    password:str

class UserResponse(BaseModel):
    id:int
    name:str
    age:int

@app.get("/users",response_model = UserResponse)
def get_user():
    return {
        "id": 1,
        "name": "Yashu",
        "age": 25,
        "password": "secret"
    }
    