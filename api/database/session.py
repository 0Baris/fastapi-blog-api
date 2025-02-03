from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL ortam değişkeni tanımlı değil.")

# print(DATABASE_URL)

# Veritabanı motoru oluştur (UTF-8 encoding ile)
engine = create_engine(DATABASE_URL, connect_args={"client_encoding": "utf8"})

# Veritabanı oturumu yönetimi
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Veritabanı oturumu oluşturup, kapatıcak fonksiyon.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()