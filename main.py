import uvicorn
from fastapi import FastAPI, Request


app = FastAPI()

@app.post('/v3/discovery:clusters')
async def clusters(request: Request):
    print(await request.json())
    return {}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)