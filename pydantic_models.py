from typing import Optional, List
from pydantic import BaseModel, Field


class DishRequestModel(BaseModel):
    is_vegan: Optional[bool] = Field(description='sign of a vegetarian dish', example=True)
    is_special: Optional[bool] = Field(description='sign of a special dish', example=True)
    topping: Optional[List] = Field(description='the dish contains additives', example=["майоне", "перец"])


class Dish(BaseModel):
    name: str = Field(description='dish name', example='Soup')
    description: str = Field(description='description of the dish', example='Very tasty')
    price: float = Field(description='dish price', example=100)
    is_vegan: bool = Field(description='sign of a vegetarian dish', example='True')
    is_special: bool = Field(description='sign of a special dish', example='True')
    toppings: List[str] = Field(description='the dish contains additives', example=["nuts", "peper"])


class DishResponseList(BaseModel):
    id: int = Field(description='Category id', example=1)
    name: str = Field(description='Category name', example='first meal')
    foods: List[Dish] = Field(description='list of dishes in this category')
