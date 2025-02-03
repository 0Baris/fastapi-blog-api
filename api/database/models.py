from sqlalchemy import String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from datetime import datetime, timezone

class Base(DeclarativeBase):
    pass

## Kullanıcı Modeli
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    ## Modeller arası ilişki.
    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="author")

## Kategori Modeli
class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(30), unique=True, index=True)

    ## Modeller arası ilişki.
    posts = relationship("Post", back_populates="category", lazy="select", cascade="all, delete-orphan" )

## Gönderi Modeli
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    title: Mapped[str] = mapped_column(String(100), index=True)
    content: Mapped[str] = mapped_column(Text, index=True)
    published: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    
    ## Modeller arası ilişki.
    author = relationship("User", back_populates="posts")
    category = relationship("Category", back_populates="posts", lazy="select")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")

## Yorum Modeli
class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    content: Mapped[str] = mapped_column(Text, index=True)
    published: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    ## Modeller arası ilişki.
    post = relationship("Post", back_populates="comments", lazy="select")
    author = relationship("User", back_populates="comments")