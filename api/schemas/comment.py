from pydantic import BaseModel
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .category import Category
    from .user import User
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
