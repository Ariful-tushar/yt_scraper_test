from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def hello_world():
    return JSONResponse(content={"message": "Hello World from FastAPI!"})

@app.post("/scrape/")
async def receive_data(request: Request):
    data = await request.json()
    user_input = data.get("input", "No input received")
    # user_input = "Hello"
    # For now, just return the received data
    return JSONResponse(content={"message": f"Received input: {user_input}"})