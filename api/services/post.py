from sqlalchemy.orm import Session, joinedload
from api.database.models import Post, Category, User


def create_post(db: Session, post_data: dict):
    """ Gönderi oluşturma fonksiyonu """
    
    # Kategori Kontrolü
    matching_category = db.query(Category).filter(Category.id == post_data["category_id"]).first()
    if not matching_category:
        raise ValueError("Belirtilen kategori bulunamadı.")
    
    # Kullanıcı Kontrolü
    matching_author = db.query(User).filter(User.id == post_data["author_id"]).first()
    if not matching_author:
        raise ValueError("Belirtilen kullanıcı bulunamadı.")
    
    ## Gelen değerleri ekleme ve güvenlik zaafiyetleri için sadece belirli alanların gönderilmesi.
    allowed_fields = {"title", "content", "category_id", "author_id", "published"}
    filtered_data = {key: value for key, value in post_data.items() if key in allowed_fields}
    
    new_post = Post(**filtered_data)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

def update_post(db:Session, post_id: int, post_data: dict):
    """ Gönderiyi güncelleme fonksiyonu. """
    matching_post = db.query(Post).filter(Post.id == post_id).first()
    if not matching_post:
        raise ValueError("Belirtilen gönderi bulunamadı.")
    
    ## Gelen değerleri güncelleme
    for key, value in post_data.items():
        if hasattr(matching_post, key):
            setattr(matching_post, key, value)
   
    db.commit()
    db.refresh(matching_post)

    return matching_post

def delete_post(db:Session, post_id: int):
    """ Gönderi silme fonksiyonu. """

    matching_post = db.query(Post).options(
        joinedload(Post.category),
        joinedload(Post.author)
    ).filter(Post.id == post_id).first()
    
    if not matching_post:
        raise ValueError("Belirtilen gönderi bulunamadı.")
    
    db.delete(matching_post)
    db.commit()

    return matching_post


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    """ Tüm gönderileri getirme fonksiyonu, limit bulundurur. """

    if skip < 0 or limit < 0:
        raise ValueError("Skip ve limit değerleri 0'dan küçük olamaz.")
    
    posts = db.query(Post).options(
        joinedload(Post.category),
        joinedload(Post.author)
    ).offset(skip).limit(limit).all()
    
    if not posts:
        raise ValueError("Belirtilen gönderi bulunamadı.")
    

    return posts


def get_post_by_id(db: Session, post_id: int):
    """ Gönderilen id ile eşleşen gönderiyi getirir. """

    db_post = db.query(Post).options(
        joinedload(Post.category),
        joinedload(Post.author)
    ).filter(Post.id == post_id).first()

    if not db_post:
        raise ValueError("Belirtilen gönderi bulunamadı.")
    
    return db_post

    
    
