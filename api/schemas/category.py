from pydantic import BaseModel
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime
from pydantic import Field

if TYPE_CHECKING:
    from .post import Post
    
class PostBase(BaseModel):
    id: int
    title: str

# Category Şeması
class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    posts: List["PostBase"] = Field(default_factory=list)

    class Config:
        from_attributes = True

## Düzenlemek için kullanılan şema.
class CategoryIn(CategoryBase):
    pass
