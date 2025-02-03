from pydantic import BaseModel
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime


if TYPE_CHECKING:
    from .category import Category
    from .comment import Comment
    
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

## Düzenlemek için kullanılan şema.
class PostIn(PostBase):
    pass

