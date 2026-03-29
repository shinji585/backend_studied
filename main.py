# mypy: ignore-errors

from fastapi import FastAPI

from todo import todo_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict: 
    return {
        "message": "Hello world"
    }
    
app.include_router(router=todo_router)