from fastapi import FastAPI

app = FastAPI()


@app.route("/")
async def hello_world():
    return {"message": "Hello World"}
