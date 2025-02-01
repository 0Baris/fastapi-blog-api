from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Veritabanı işlemleri
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

# Veritabanı oturumu oluşturup, kapatıcak fonksiyon.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()