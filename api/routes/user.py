from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.session import get_db
from api.schemas.user import UserCreate, User
from api.services.user import create_user, get_user_by_id, get_users, get_user_by_email
from api.tasks.email import send_email
from typing import List
from api.utils.email_checker import checker

router = APIRouter()

@router.post("/", response_model=User)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """ Yeni kullanıcı oluşturur. """
    mail = user.email
    
    existing_user = get_user_by_email(db, email=mail)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email halihazırda kayıtlı!")
    
    if checker(mail):
        subject = f"Hoşgeldin!, {user.username} | BlogAPI"
        body = f"Merhaba {user.username}, Sitemize kayıt olduğun için teşekkür ederiz. Bu bir celery denemesidir!"
        send_email.delay(subject=subject, user_email=mail, message_body=body)
        
        return create_user(db, user.dict())
    else:
        raise HTTPException(status_code=400, detail="Email adresiniz geçersiz.")


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
