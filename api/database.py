from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# SQLALCHEMY_DATABASE_URL = "postgresql://kullanıcıadı:sifre@localhost/veritabanıismi" -- PostgreSQL Bağlantısı

# SQlite geliştirme için yeterli.
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

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