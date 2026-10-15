from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

URL="https://dummyjson.com/posts"

# GET ALL
@app.get("/posts")
def get_posts():
    response = requests.get(URL)
    return response.json()

#GET Single
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    response = requests.get(f"{URL}/{post_id}")

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Data not found")

    return response.json()