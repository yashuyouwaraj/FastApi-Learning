from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# import os
# from dotenv import load_dotenv
from config import settings

app = FastAPI()

# load_dotenv()

#Allowed Origins(Front-end URl)
origins = settings.origins
# SECRET_KEY= os.getenv("SECRET_KEY")
# DB_URL = os.getenv("DB_URL")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_origins=origins
)

@app.get("/")
def home():
    return {
        "message":"CORS ENABLE API"
    }