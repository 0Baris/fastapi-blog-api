from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.session import get_db
from api.schemas.user import UserCreate, User
from api.services.user import create_user, get_user_by_id, get_users, get_user_by_email
from typing import List

router = APIRouter()

@router.post("/", response_model=User)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """ Yeni kullanıcı oluşturur. """
    existing_user = get_user_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email halihazırda kayıtlı!")
    
    return create_user(db, user.dict())

@router.get("/", response_model=List[User])
def users(skip: int=0, limit: int = 100, db: Session = Depends(get_db)):
    """ Tüm kullanıcıları listeler. """
    try:
        return get_users(db, skip, limit)
    except:
        raise HTTPException(status_code=404, detail="Kullanıcı listesi bulunamadı!")

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """ ID'si eşleşen kullanıcıyı getirir. """
    try:
        return get_user_by_id(db, user_id)
    except:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı.")
