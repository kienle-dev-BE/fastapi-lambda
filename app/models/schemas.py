from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    ProductId: Optional[str]
    ProductName: str
    Price: str
    StockLevel: int
    imageUrl: Optional[str]

class Order(BaseModel):
    ProductId: str
    Quantity: int
