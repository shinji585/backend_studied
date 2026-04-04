# mypy: ignore-errors

from fastapi import FastAPI

from todo import todo_router

app = FastAPI()

    
app.include_router(router=todo_router)