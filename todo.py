from fastapi import APIRouter, Path, Query, HTTPException, status
from model import Todo, TodoUpdate, TodoItems

todo_router = APIRouter()

todo_list: list[Todo] = []


@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}


@todo_router.get("/todo", response_model=TodoItems)
async def get_todo() -> dict:
    
    if len(todo_list) == 0: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No todos found"
        )
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

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exits"
    )


@todo_router.get("/search")
async def search_todo(query: str = Query(..., title="Search todo")) -> dict:
    match_: list = []
    for todo in todo_list:
        if todo.title == query:
            match_.append(todo)
    if  match_:
        return {"results": match_}
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo is not on the db"
    )
    
    
# using update method -> path 
@todo_router.patch("/todo/{id}")
async def update_data(todoUpdate: TodoUpdate, id: int = Path(...,title="the ID of the todo to be updated")) -> dict: 
    for todo in todo_list: 
        if todo.id == id:
            if todoUpdate.title is not None: 
                todo.title = todoUpdate.title
            
            if todoUpdate.item is not None: 
                todo.item = todoUpdate.item
                
            return {"message": "Todo partially updated"}
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo not found"
    )
            
            
@todo_router.put("/todo/{id}")
async def update_data_everything(todoUpdate: TodoUpdate, id: int = Path(...,title="he ID of the todo to be updated")) -> dict: 
    for todo in todo_list: 
        if todo.id == id: 
            todo.title = todoUpdate.title if todoUpdate.title is not None else todo.title
            todo.item = todoUpdate.item if todoUpdate.item is not None else todo.item
            return {"message": "Todo all Updated"}
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo not found"
    )