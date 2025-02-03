from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.session import get_db
from api.schemas.comment import Comment, CommentCreate
from api.services.comment import create_comment, delete_comment
from typing import List

router = APIRouter()

@router.post("/{post_id}/add", response_model=Comment)
def add_comment(post_id: int, comment_data: CommentCreate, db: Session = Depends(get_db)):
    """Belirtilen gönderiye yorum ekler."""
    try:
        return create_comment(db, post_id, comment_data.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{post_id}/delete", response_model=Comment)
def del_comment(post_id: int, db: Session = Depends(get_db)):
    """ ID'si eşleşen yorumu siler. """
    try:
        return delete_comment(db, post_id)
    except:
        raise HTTPException(status_code=404, detail="Gönderi bulunamadı.")  