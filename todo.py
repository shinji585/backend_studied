from fastapi import APIRouter, Depends, Path, Query, HTTPException, Request, status
from model import Todo, TodoUpdate
from fastapi.templating import Jinja2Templates

# response_model is not used with jinja 

todo_router = APIRouter()

todo_list: list[Todo] = []


# this mean all my HTML templates live inside /templates
templates = Jinja2Templates(directory="templates/")

@todo_router.post("/web/todo")
async def add_todo(request: Request,todo: Todo = Depends(Todo.as_form)):
    todo.id = max([t.id for t in todo_list if t.id is not None], default=0) + 1 
    todo_list.append(todo)
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "todos": todo_list
    })


@todo_router.get("/web/todo")
async def get_todo(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "todos": todo_list
    })



@todo_router.post("/web/todo/list")
async def add_todo_list(request: Request, todos: list[Todo]):
    
    try: 
        for todo in todos:
            todo_list.append(todo)
    except Exception: 
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to add todo"
        )        
                
    return templates.TemplateResponse("index.html",{
        "request": request,
        "todos": todo_list
    })
    

@todo_router.get("/web/todo/{todo_id}")
async def get_single_todo(request: Request, todo_id: int = Path(..., gt=0)):

    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse("index.html", {
                "request": request,
                "todo": [todo]
            })

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

@todo_router.get("/web/search")
async def search_todo(request: Request, query: str = Query(...)):

    match_ = [todo for todo in todo_list if todo.title == query]

    if match_:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "results": match_
        })

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )
    
    
# using update method -> path 
@todo_router.patch("/web/todo/{id}")
async def update_data(
    request: Request,
    todoUpdate: TodoUpdate,
    id: int = Path(..., title="The ID of the todo to be updated", gt=0)
):
    for todo in todo_list:
        if todo.id == id:

            if todoUpdate.title is not None:
                todo.title = todoUpdate.title

            if todoUpdate.item is not None:
                todo.item = todoUpdate.item

            return templates.TemplateResponse("index.html", {
                "request": request,
                "todos": todo_list
            })

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )
            
            
@todo_router.put("/web/todo/{id}")
async def update_data_everything(
    request: Request,
    todoUpdate: TodoUpdate,
    id: int = Path(..., title="The ID of the todo to be updated", gt=0)
):
    for todo in todo_list:
        if todo.id == id:
            todo.title = todoUpdate.title if todoUpdate.title is not None else todo.title
            todo.item = todoUpdate.item if todoUpdate.item is not None else todo.item

            return templates.TemplateResponse("index.html", {
                "request": request,
                "todos": todo_list
            })

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )