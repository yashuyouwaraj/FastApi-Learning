from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class TodoInput(BaseModel):
    title: str
    completed: bool = False


class Todo(TodoInput):
    id: int


todos: dict[int, Todo] = {}


@app.get("/todos", response_model=list[Todo])
def get_todos():
    return list(todos.values())


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )
    return todo


@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoInput):
    todo_id = max(todos, default=0) + 1
    new_todo = Todo(id=todo_id, **todo.model_dump())
    todos[todo_id] = new_todo
    return new_todo


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: TodoInput):
    if todo_id not in todos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )

    updated_todo = Todo(id=todo_id, **todo.model_dump())
    todos[todo_id] = updated_todo
    return updated_todo


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )
    del todos[todo_id]