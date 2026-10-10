from fastapi import FastAPI

app = FastAPI()

@app.post("/create-users")
def create_user(user:dict):
    return {
        "message":"User created successfully",
        "data": user
    }
