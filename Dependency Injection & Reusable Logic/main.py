from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

def common_logic():
    return {
        "message":"This is common logic"
    }

def get_current_user():
    return {
        "user":"Yashu"
    }
    
def verify_token(token:str= Header(None)):
    if token != "mytoken":
        raise HTTPException(
            status_code= 401,
            detail="Invalid Token"
        )
    return {
        "user":"Authorized User"
    }
    
    
@app.get("/home")
def home(data = Depends(common_logic)):
    return data


@app.get("/profile")
def profile(user= Depends(get_current_user)):
    return user

@app.get("/dashboard")
def dashboard(data = Depends(get_current_user), common = Depends(common_logic)):
    return {
        "user":data,
        "common":common
    }
    

@app.get("/secure")
def secure_data(data = Depends(verify_token)):
    return data