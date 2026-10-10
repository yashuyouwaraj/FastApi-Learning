from fastapi import FastAPI

app = FastAPI()

#optional parameters
@app.get("/user")
def get_user(user_id: int = None):
    return {
        "user_id": user_id
    }

#Default parameters
@app.get("/item")
def get_name(name: str = "Yashu"):
    return {
        "name":name
    }

#Multiple query parameters
#http://127.0.0.1:8000/items?name=Iphone&price=2000'
@app.get("/items")
def get_items(name: str = "Iphone", price: int = 2000):
    return {
        "name": name,
        "price": price
    }