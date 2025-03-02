from fastapi import FastAPI
import uvicorn  # ASGI server to run FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI with Poetry!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
