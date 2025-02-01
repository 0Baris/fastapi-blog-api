from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload, noload
from api.database import engine, SessionLocal, get_db
from typing import List
from api import  schemas, hashing
from api.models import User, Category, Post, Comment, Base
from datetime import datetime


app = FastAPI()

@app.get("/health/", status_code=200)
def health_check():
    return {"status": "ok"}

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
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    if not users:
        raise HTTPException(status_code=404, detail="Kullanıcı listesi bulunamadı!")
    return [schemas.User.from_orm(user) for user in users ]

## Tekil üye getirme
@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Belirtilen kullanıcı bulunamadı.")
    
    return schemas.User.from_orm(user)


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
    ## İstenilen değer için query sorgusu
    category = db.query(Category).offset(skip).limit(limit).all()
    
    if not category:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı")
    return [schemas.Category.from_orm(ctg) for ctg in category ]


## Tekil kategori getirme.
@app.get("/category/{category_id}", response_model=schemas.Category)
def get_category(category_id: int ,db: Session = Depends(get_db)):
    ## İstenilen değer için query sorgusu
    category = db.query(Category).filter(Category.id == category_id).first()
    
    if not category:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı")
    
    return schemas.Category.from_orm(category)


## Kategori düzenleme
@app.put("/category-update/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category_data: schemas.CategoryIn , db: Session = Depends(get_db)):
    ## İstenilen değer için query sorgusu
    category = db.query(Category).filter(Category.id == category_id).first()
    
    if not category:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı")

    category.title = category_data.title
    db.commit()  # Değişiklikleri kaydet
    db.refresh(category)  # Güncellenmiş veriyi al

    return schemas.Category.from_orm(category)


## Kategori silme
@app.delete("/category-delete/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    ## İstenilen değer için query sorgusu
    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı")
    
    db.delete(category)
    db.commit()

    return schemas.Category.from_orm(category)

## Gönderi oluşturma
@app.post("/posts/", response_model=schemas.PostCreate)
def add_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # Kullanıcı Kontrolü
    author = db.query(User).filter(User.id == post.author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Kullanıcı Bulunmadı!")

    # Kategori Kontrolü
    category_id = db.query(Category).filter(Category.id == post.category_id).first()
    if not category_id:
        raise HTTPException(status_code=404, detail="Belirtilen kategori geçersiz.")

    new_post = Post(
        title=post.title,
        content=post.content,
        category_id=post.category_id,
        author_id=post.author_id,
        published=datetime.utcnow()
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    ## Gönderinin alınması, hata üzerine eklenmiştir ##
    loaded_post = db.query(Post).options(
        joinedload(Post.category),
        joinedload(Post.author)
    ).filter(Post.id == new_post.id).first()

    if not loaded_post:
        raise HTTPException(status_code=500, detail="Yazı veritabanından yüklenemedi.")


    ## In dev logs
    # print("Loaded Post:", loaded_post)
    # print("Category ID:", loaded_post.category_id)
    # print("Author ID:", loaded_post.author_id)

    return schemas.Post.from_orm(loaded_post)

## Tüm gönderileri getirme.
@app.get("/posts/", response_model=List[schemas.Post])
def get_posts(skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    posts = db.query(Post).offset(skip).limit(limit).all()

    if not posts:
        raise HTTPException(status_code=404, detail="Gönderi listesi bulunamadı!")
    
    return [schemas.Post.from_orm(post) for post in posts]

## Tekil gönderi getirme.
@app.get("/posts/{post_id}", response_model=schemas.Post)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    
    if not post:
        raise HTTPException(status_code=404, detail="Belirtilen gönderi bulunamadı.")

    return schemas.Post.from_orm(post)

## Gönderi güncelleme.
@app.put("/posts-update/{post_id}", response_model=schemas.PostIn)
def update_post(post_id: int, post_data: schemas.PostIn, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    
    if not post:
        raise HTTPException(status_code=404, detail="Belirtilen gönderi bulunamadı.")

    post.title = post_data.title
    post.content = post_data.content
    db.commit()
    db.refresh(post)

    return schemas.Post.from_orm(post)

## Gönderi silme.
@app.delete("/posts-delete/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).options(joinedload(Post.category), joinedload(Post.author)).filter(Post.id == post_id).first()
    
    if not post:
        raise HTTPException(status_code=404, detail="Belirtilen gönderi bulunamadı.")

    deleted_post = schemas.Post.model_validate(post)
    db.delete(post)
    db.commit()

    return deleted_post

## Yorum ekleme.
@app.post("/posts/{post_id}/add-comment", response_model=schemas.CommentCreate)
def add_comment(post_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):

    author = db.query(User).filter(User.id == comment.author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Kullanıcı Bulunmadı!")

    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Yorum atmak istediğiniz gönderi bulunamadı.")

    new_comment = Comment(
        content=comment.content,
        author_id=comment.author_id,
        post_id=post_id
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    loaded_comment = db.query(Comment).options(
        joinedload(Comment.post).options(noload(Post.comments)),
        joinedload(Comment.author)
    ).filter(Comment.id == new_comment.id).first()

    if not loaded_comment:
        raise HTTPException(status_code=500, detail="Yorum veritabanından yüklenemedi.")

    return schemas.Comment.from_orm(loaded_comment)

## Yorum silme.
@app.delete("/posts/{post_id}/delete-comment", response_model=schemas.Comment)
def delete_comment(post_id: int, db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.id == post_id).first()

    if not comment:
        raise HTTPException(status_code=404, detail="Yorum bulunamadı")
    
    db.delete(comment)
    db.commit()

    return schemas.Comment.from_orm(comment)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "create-tables":
        Base.metadata.create_all(bind=engine)
        print("Tablolar başarıyla oluşturuldu.")
    else:
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)