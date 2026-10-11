from fastapi import FastAPI, status, HTTPException

app = FastAPI()

@app.post("/create_user",status_code = status.HTTP_201_CREATED)
def create_user():
    return {
        "message":"User Created"
    }
    
@app.get("/user")
def get_users():
    return {
        "status": "Success",
        "message": "User Found",
        "data":{
            "name":"Yashu",
            "age":25
        }
    }
    
@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id == 1:
        return {
            "status": "Success",
            "message": "User Found",
            "data":{
                "name":"Yashu",
                "age":25
            }
        }
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"User with id {user_id} not found")