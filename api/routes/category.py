from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.session import get_db
from api.schemas.category import Category, CategoryCreate, CategoryIn
from api.services.category import create_category, update_category, delete_category
from api.services.category import get_category, get_category_by_id
from typing import List

router = APIRouter()


@router.post("/", response_model=Category)
def register_category(category: CategoryCreate, db: Session = Depends(get_db)):
    """ Yeni kategori oluşturur. """
    return create_category(db, category.dict())

@router.put("/update/{category_id}", response_model=Category)
def edit_category(category_id: int, category_data: CategoryIn ,db: Session = Depends(get_db)):
    """ ID'si eşleşen kategoriyi günceller. """
    try:
        return update_category(db, category_id, category_data.dict())
    except:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı.")

@router.delete("/delete/{category_id}", response_model=Category)
def del_category(category_id: int, db: Session = Depends(get_db)):
    """ ID'si eşleşen kategoriyi siler. """
    try:
        return delete_category(db, category_id)
    except:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı.")

@router.get("/", response_model=List[Category])
def category_list(skip: int=0, limit: int = 100, db: Session = Depends(get_db)):
    """ Tüm kategorileri listeler. """
    try:
        return get_category(db, skip, limit)
    except:
        raise HTTPException(status_code=404, detail="Kategori listesi bulunamadı!")

@router.get("/{category_id}", response_model=Category)
def category(category_id: int, db: Session = Depends(get_db)):
    """ ID'si eşleşen kategoriyi getirir. """
    try:
        return get_category_by_id(db, category_id)
    except:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı.")
