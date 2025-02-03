from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Category Şeması
class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True

## Düzenlemek için kullanılan şema.
class CategoryIn(CategoryBase):
    pass
