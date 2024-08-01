from fastapi import FastAPI
from routers import user_router

app = FastAPI()

app.include_router(user_router.router, prefix="/api", tags=["users"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI with MongoDB CRUD project"}
