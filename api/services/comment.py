from sqlalchemy.orm import Session, joinedload
from api.database.models import Comment, Post, User
from datetime import datetime



def create_comment(db: Session, post_id: int, comment_data: dict):
    """Yeni bir yorum oluşturur."""
    # Gönderi kontrolü
    matching_post = db.query(Post).filter(Post.id == post_id).first()
    if not matching_post:
        raise ValueError("Belirtilen gönderi bulunamadı.")
    
    # Kullanıcı kontrolü
    matching_author = db.query(User).filter(User.id == comment_data["author_id"]).first()
    if not matching_author:
        raise ValueError("Belirtilen kullanıcı bulunamadı.")
    
    # Yeni yorumu oluştur
    new_comment = Comment(**comment_data, post_id=post_id, published=datetime.utcnow())
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def delete_comment(db: Session, comment_id: int):
    """ Yorum silme fonksiyonu """
    comment = db.query(Comment).options(
        joinedload(Comment.post),
        joinedload(Comment.author),
    ).filter(Comment.id == comment_id).first()

    if not comment:
        raise ValueError("Belirtilen yorum mevcut değil.")
    
    db.delete(comment)
    db.commit()

    return comment