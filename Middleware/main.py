from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def my_middleware(request: Request, next):
    print("Request received")
    response = await next(request)
    print("Response sent")
    return response


@app.middleware("http")
async def log_middleware(request: Request, next):
    start_time = time.time()
    response = await next(request)
    process_time = time.time() - start_time
    print(f"Path: {request.url.path} | Request processing time: {process_time} seconds")
    return response