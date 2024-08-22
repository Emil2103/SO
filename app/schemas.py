from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductInCategory(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Category(CategoryBase):
    id: int
    products: List[ProductInCategory] = []

    class Config:
        orm_mode = True

class Product(ProductBase):
    id: int
    category: Optional[CategoryBase] = None

    class Config:
        orm_mode = True

