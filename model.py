from typing import Optional

from pydantic import BaseModel

from fastapi import Form

class Item(BaseModel):
    item: str
    status: str

    class Config:
        schema_extra = {"example": {"item": "Go to the gym", "stauts": "Uncompleted"}}


class Todo(BaseModel):
    id: Optional[int] = None
    title: str
    item: Item
    
    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        item: str = Form(...),
        status: str = Form(...)
    ):
        return cls(
            title=title,
            item=Item(item=item,status=status)
        )

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
