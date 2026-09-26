from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing import Optional
from fastapi import FastAPI

class Product(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)
    category: str
    sku: str = Field(min_length=5, max_length=20)
    email: EmailStr
    stock: bool = True
    discount_price : Optional[float] = None
    @field_validator('name')
    @classmethod
    def validate_name(cls, value):
        return value.strip()
    @field_validator('sku')
    @classmethod
    def validate_sku(cls, value):
        if ' ' in value:
            raise ValueError('SKU can not contain spaces')
        return value.upper()
    @model_validator(mode = 'after')
    def discount_validator(self):
        if self.discount_price is not None and self.discount_price >= self.price:
            raise ValueError('Discount price must be lower that normal price')
        return self
    
class ProductResponse(BaseModel):
        name: str = Field(min_length=3, max_length=100)
        price: float = Field(gt=0)
        quantity: int = Field(ge=0)
        category: str
        stock: bool = True
        discount_price : Optional[float] = None
app = FastAPI()

@app.post('/products', response_model = ProductResponse)
def create_product(product: Product):
        return product


    