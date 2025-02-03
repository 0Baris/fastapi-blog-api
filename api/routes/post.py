from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.session import get_db
from api.schemas.post import Post, PostCreate, PostIn
from api.services.post import create_post, update_post, delete_post
from api.services.post import get_post_by_id, get_posts
from typing import List

router = APIRouter()

@router.post("/", response_model=Post)
def register_post(post: PostCreate, db: Session = Depends(get_db)):
    """ Yeni gönderi oluşturur. """
    return create_post(db, post.dict())

@router.put("/update/{post_id}", response_model=Post)
def edit_category(post_id: int, post_data: PostIn ,db: Session = Depends(get_db)):
    """ ID'si eşleşen gönderiyi günceller. """
    try:
        return update_post(db, post_id, post_data.dict())
    except:
        raise HTTPException(status_code=404, detail="Düzenlenmek isteyen gönderi bulunamadı.")

@router.delete("/delete/{post_id}", response_model=Post)
def del_post(post_id: int, db: Session = Depends(get_db)):
    """ ID'si eşleşen gönderiyi siler. """
    try:
        return delete_post(db, post_id)
    except:
        raise HTTPException(status_code=404, detail="Silinmek istenen gönderi bulunamadı.")

@router.get("/", response_model=List[Post])
def post_list(skip: int=0, limit: int = 100, db: Session = Depends(get_db)):
    """ Tüm gönderileri listeler. """
    try:
        return get_posts(db, skip, limit)
    except:
        raise HTTPException(status_code=404, detail="Gönderi listesi bulunamadı!")

@router.get("/{post_id}", response_model=Post)
def post(post_id: int, db: Session = Depends(get_db)):
    """ ID'si eşleşen gönderiyi getirir. """
    try:
        return get_post_by_id(db, post_id)
    except:
        raise HTTPException(status_code=404, detail="Gönderi bulunamadı.")
