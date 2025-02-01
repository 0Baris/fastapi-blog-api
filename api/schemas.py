from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# User Şeması
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    posts: List["Post"] = [] 
    comments: List["Comment"] = []

    class Config:
        from_attributes = True

# Category Şeması
class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True

class CategoryIn(CategoryBase):
    pass

# Post Şeması
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    category_id: int
    author_id: int

class Post(PostBase):
    id: int
    published: datetime
    category_id: int
    author_id: int
    category: Optional["Category"]
    comments: List["Comment"] = [] 

    class Config:
        from_attributes = True

class PostIn(PostBase):
    pass

# Comment Şeması
class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    author_id: int

class Comment(CommentBase):
    id: int
    published: datetime
    author_id: int

    class Config:
        from_attributes = True

# İleri Referansları Çözme
User.update_forward_refs()
Category.update_forward_refs()
Post.update_forward_refs()
Comment.update_forward_refs()