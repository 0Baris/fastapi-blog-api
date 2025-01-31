from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, get_db
from typing import List
from . import  schemas, hashing
from .models import User, Category, Post, Comment, Base

# Database oluşturma.
Base.metadata.create_all(bind= engine) 

app = FastAPI()

## Üye oluşturma
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Email kontrolü
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Parolayı hashleme
    hashed_password = hashing.hash_password(user.password)
    
    new_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password,
        is_active=True
    ) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return schemas.User.from_orm(new_user)

## Tüm üyeleri getirme
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    if not users:
        raise HTTPException(status_code=404, detail="Users not found!")
    return [schemas.User.from_orm(user) for user in users ]

## Tekil üye getirme
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return schemas.User.from_orm(db_user)


## Kategori ekleme
@app.post("/category/", response_model=schemas.CategoryCreate)
def add_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    # Kategori kontrolü
    existing_category = db.query(Category).filter(Category.title == category.title).first()
    
    if existing_category:
        raise HTTPException(status_code=400, detail="Kategori halihazırda mevcut")
    
    new_category = Category(
        title=category.title,
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    
    return schemas.Category.from_orm(new_category)


## Kategori Listeleme
@app.get("/category/", response_model=list[schemas.Category])
def get_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    category = db.query(Category).offset(skip).limit(limit).all()
    
    if not category:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı")
    return [schemas.Category.from_orm(ctg) for ctg in category ]


## Tekil kategori getirme.
@app.get("/category/{category_id}", response_model=schemas.Category)
def get_category(category_id: int ,db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == category_id).first()
    
    if not category:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı")
    
    return schemas.Category.from_orm(category)


## Kategori düzenleme
@app.put("/category-update/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, payload:schemas.CategoryIn , db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == category_id).first()
    
    if not category:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı")

    update_data = payload.dict(exclude_unset=True)

    category.filter(Category.id == category_id).update(update_data,
                                                       synchronize_session=False)

    return schemas.Category.from_orm(category)


## Kategori silme
@app.delete("/category-delete/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, payload: schemas.Category , db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı")
    
    return schemas.Category.from_orm(category)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")