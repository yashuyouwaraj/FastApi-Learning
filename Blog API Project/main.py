from fastapi import FastAPI,Depends,HTTPException,Query
from sqlalchemy.orm import Session
from database import engine,SessionLocal
import model,schemas

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#Home
@app.get("/")
def home():
    return{
        "message":"Blog API Started"
    }


#Create Blog
@app.post("/blogs",response_model= schemas.BlogResponse)
def create_blog(blog:schemas.BlogCreate, db:Session = Depends(get_db)):
    new_blog = model.Blog(
        title = blog.title,
        content = blog.content
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog


#Read All Blog
@app.get("/blogs",response_model=list[schemas.BlogResponse])
def get_blogs(db: Session= Depends(get_db)):
    return db.query(model.Blog).all()

#Read One Blog
@app.get("/blogs/{id}",response_model= schemas.BlogResponse)
def get_blog(id:int, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    return blog

#Update Blog
@app.put("/blogs/{id}",response_model=schemas.BlogResponse)
def update_blog(id:int, blog:schemas.BlogCreate, db: Session = Depends(get_db)):
    existingblog = db.query(model.Blog).filter(model.Blog.id == id).first()
        
    if not existingblog:
        raise HTTPException(status_code=404, detail="Blog not found")
        
    existingblog.title = blog.title
    existingblog.content = blog.content
    
    db.commit()
    
    return existingblog

#Delete Blog
@app.delete("/blogs/{id}")
def delete_blog(id:int, db:Session = Depends(get_db)):
    existing_blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    
    if not existing_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    db.delete(existing_blog)
    
    db.commit()
    
    return{
        "message":"Blog deleted Successfully"
    }