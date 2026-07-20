from decimal import Decimal

from pydantic import BaseModel


class NewProductRequest(BaseModel):
    name : str
    description: str
    price : Decimal
    stock_quantity : int
    category : str

class UpdateProductRequest(BaseModel):
    product_id : int
    name: str
    description: str
    price: Decimal
    stock_quantity: int
    category: str