from typing import Optional, List

from pydantic import BaseModel


class DishesRequest(BaseModel):
    is_vegan: Optional[bool]
    is_special: Optional[bool]
    topping: Optional[List[int]]
