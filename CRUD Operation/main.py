from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


todos = []


class Todo(BaseModel):
    id: int
    title: str
    completed: bool


@app.get("/todos")
def get_todos():
    return {
        "message": "Todos fetched successfully",
        "data": todos,
    }


@app.post("/todos")
def create_todo(todo: Todo):
    for existing_todo in todos:
        if existing_todo.id == todo.id:
            return {
                "message": "Todo already exists",
                "data": existing_todo,
            }

    todos.append(todo)
    return {
        "message": "Todo created successfully",
        "data": todo,
    }


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {
                "message": "Todo fetched successfully",
                "data": todo,
            }
    return {"message": "Todo not found"}


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return {
                "message": "Todo updated successfully",
                "data": updated_todo,
            }
    return {"message": "Todo not found"}


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[i]
            return {"message": "Todo deleted successfully"}
    return {"message": "Todo not found"}

