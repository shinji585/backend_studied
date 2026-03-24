# mypy: ignore-errors

from fastapi import APIRouter
from fastapi import FastAPI

countries_router = APIRouter()

coutries: list = []

@countries_router.get("/countries")
async def get_countries() -> list: 
    return coutries

@countries_router.post("/countries")
async def post_countries(dato: dict) -> dict: 
    coutries.append(dato)
    return {"message": f"country added: {dato}"} 


app = FastAPI()

app.include_router(countries_router)