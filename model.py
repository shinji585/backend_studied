from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    item: str
    status: str

    class Config:
        schema_extra = {"example": {"item": "Go to the gym", "stauts": "Uncompleted"}}


class Todo(BaseModel):
    id: int
    title: str
    item: Item

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Gym PR",
                "item": {"item": "Squat 150kg", "status": "Uncompleted"},
            }
        }


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    item: Optional[Item] = None

    class Config:
        schema_extra = {"example": {"title": "Update title"}}


class TodoItems(BaseModel):
    todos: list[Todo]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "id": 1,
                        "title": "Gym PR",
                        "item": {"item": "Squat 150kg", "status": "Uncompleted"},
                    },
                    {
                        "id": 2, 
                        "title": "Study Exercises",
                        "item": {"item": "solved 3 exercises of linear algebra", "status": "Completed"}
                    }
                ]
            }
        }
