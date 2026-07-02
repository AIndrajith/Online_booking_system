import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app:FastAPI):
    # create tables
    init_models()
    yield

app = FastAPI(
    title="Daraz online shopping",
    lifespan=lifespan
)

app.include_router(router)

@app.get("/")
def home():
    return {"message":"API running"}

if __name__ == "__main__":
    uvicorn.run(app.host="127.0.0.1", port=8000)