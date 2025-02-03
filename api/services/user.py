from sqlalchemy.orm import Session
from api.database.models import User
from api.utils.hashing import hash_password

def create_user(db: Session, user_data: dict):
    """ Kullanıcı oluşturma fonksiyonu, parolayı hashler. """

    # Şifreyi hashle.
    hashed_password = hash_password(user_data.pop("password", None))
    if not hashed_password:
        raise ValueError("Parola eksik veya geçersiz.")
    
    # Hashlenmiş şifreyi kaydet.
    user_data["hashed_password"] = hashed_password

    new_user = User(**user_data)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """ Tün kullanıcıları getirme fonksiyonu, limit bulundurur. """
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    """ Gönderilen email ile eşleşen kullanıcı var ise kayıt işlemi gerçekleşmez. """
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, id: int):
    """ Gönderilen id ile eşleşen kullanıcıyı getirir. """
    return db.query(User).filter(User.id == id).first()
