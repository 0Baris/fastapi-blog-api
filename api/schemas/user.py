from pydantic import BaseModel
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .post import Post
    from .comment import Comment

# Kullancı şeması
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
