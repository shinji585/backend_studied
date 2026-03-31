from typing import Optional

from pydantic import BaseModel

class Item(BaseModel): 
    item: str
    status: str 

class Todo(BaseModel): 
    id: int 
    title: str 
    item: Item

class TodoUpdate(BaseModel): 
    title: Optional[str] = None 
    item: Optional[Item] = None