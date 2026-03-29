from fastapi import APIRouter, Path, Query
from model import Todo

todo_router = APIRouter()

todo_list: list[Todo] = []


@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}


@todo_router.get("/todo")
async def get_todo() -> dict:
    return {"todos": todo_list}


@todo_router.post("/todo/list")
async def add_todo_list(todos: list[Todo]) -> dict:
    for todo in todos:
        todo_list.append(todo)
    return {"message": "Todos added successfully"}


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    todo_id: int = Path(..., title="The ID for the todo to retrieve.", gt=0),
) -> dict:

    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}

    return {"message": "Todo with supplied ID doesn't exits."}


@todo_router.get("/search")
async def search_todo(query: str = Query(..., title="Search todo")) -> dict:
    match_: list = []
    for todo in todo_list:
        if todo.title == query:
            match_.append(todo.item)
    if  match_:
        return {"results": match_}
    else:
        return {"message": "Todo is not on the db"}