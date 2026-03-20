# in this section you will find a server made using fasstapi and here is where the things studied before start to have meaning 
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Country(BaseModel): 
    country_id: Optional[int] = Field(default=None,alias="id")
    name: str 
    capital: str 
    area: int 
    
countries: list[Country] = []

def _get_next_id() -> int:
    valid_ids = [c.country_id for c in countries if c.country_id is not None]
    if not valid_ids: 
        return 1  
    return max(valid_ids) + 1 

def _create_country(data: dict) -> Country: 
    new_country = Country(
        id=_get_next_id(),
        **data
    )
    countries.append(new_country)
    return new_country

# endpoints 

@app.get("/")
async def main(): 
    return FileResponse('index.html')

@app.get("/countries")
async def get_countries(): 
    return countries

@app.post("/countries",status_code=201)
async def add_country(country: dict): 
    clean_data = {k: v for k,v in country.items() if k != "id"}
    new_country = _create_country(clean_data)
    return new_country