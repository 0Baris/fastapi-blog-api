from sqlalchemy.orm import Session, joinedload
from api.database.models import Category


def create_category(db: Session, category_data: dict):
    """ Kategori oluşturma fonksiyonu. """
    matching_category = db.query(Category).filter(Category.title == category_data["title"]).first()
    if matching_category:
        raise ValueError("Belirtilen kategori halihazırda mevcut!")
    
    new_category = Category(**category_data)

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def update_category(db: Session, category_id: int, updated_category: dict):
    """ Gönderilen id ile eşleşen bir kategori varsa onun adını düzenler. """

    matching_category = db.query(Category).filter(Category.id == category_id).first()
    if not matching_category:
        raise ValueError("Belirtilen kategori bulunamadı.")
    
    for key, value in updated_category.items():
        if hasattr(matching_category, key):
            setattr(matching_category, key, value)

    db.commit()
    db.refresh(matching_category)

    return matching_category

def delete_category(db: Session, category_id: int):
    """ Gönderilen id ile eşleşen bir kategori varsa siler. """
    matching_category = db.query(Category).options(
        joinedload(Category.posts),
    ).filter(Category.id == category_id).first()

    if not matching_category:
        raise ValueError("Belirtilen kategori bulunamadı.")
    
    db.delete(matching_category)
    db.commit()

    return matching_category

def get_category(db: Session, skip: int = 0, limit: int = 100):
    """ Tüm kategorileri getirme fonksiyonu, limit bulundurur. """
    if skip < 0 or limit < 0:
        raise ValueError("Skip ve limit değerleri 0'dan küçük olamaz.")
    categories = db.query(Category).offset(skip).limit(limit).all()
    return categories

def get_category_by_id(db: Session, id: int):
    """ Gönderilen id ile eşleşen kategoriyi getirir. """
    category = db.query(Category).filter(Category.id == id).first()
    return category
