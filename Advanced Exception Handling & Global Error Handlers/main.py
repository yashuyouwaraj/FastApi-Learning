from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFountException(Exception):
    def __init__(self,name:str):
        self.name = name

@app.exception_handler(UserNotFountException)
def user_not_found_handler(request:Request, exc:UserNotFountException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"User {exc.name} not found"
        }
    )

@app.get("/user/{name}")
def get_user(name:str):
    if name != "yashu":
        raise UserNotFountException(name)
    return{
        "name":name
    }

@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code= 404,
            detail="User Not Found"
        )
    return{
        "id":1,
        "name":"Yashu"
    }