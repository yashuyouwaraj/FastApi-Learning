from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

app = FastAPI()

# Database URL
DATABASE_URL = "sqlite:///./test.db"

# Engine create (DB connection)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Session (DB operations ke liye)
SessionLocal = sessionmaker(bind=engine)

# Base (model ke liye)
Base = declarative_base()


# Table (Model)
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)


# Table create
Base.metadata.create_all(bind=engine)


# Dependency (DB session provide karega)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Create API
@app.post("/todos")
def create_todo(title:str,db: Session = Depends(get_db)):
    todo = Todo(title=title,completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Created",
        "data":todo
    }

#Get All Data
@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return{
        "message":"Todos fetched",
        "Total":len(todos),
        "data":todos
    }

#Get Single Data By Id
@app.get("/todos/{id}")
def get_todo(id:int, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return{
        "message":"Todo fetched",
        "data": todo
    }
    
#Update a data
@app.put("/todos/{id}")
def update_todo(id:int, title:str, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo.title = title
    
    db.commit()
    db.refresh(todo)
    
    return {
        "message":"Todo Updated",
        "data": todo
    }