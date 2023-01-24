from typing import List

from fastapi import FastAPI

from crud import get_dishes_list, select_topping
from pydantic_models import DishRequestModel, Dish, DishResponseList

app = FastAPI()


@app.post("/dish/", response_model=List[DishResponseList])
async def dish(request: DishRequestModel) -> List[DishResponseList]:
    """
    Returns a list of dishes grouped by category.
    :param request: DishRequestModel
    :return: List[DishResponseList]
    """
    e = request.is_vegan
    dishes = await get_dishes_list(request.topping, is_vegan=request.is_vegan, is_special=request.is_special)
    category_dict = {}
    for dish in dishes:
        dish_model = Dish(
            name=dish.food_name,
            description=dish.description,
            price=dish.price,
            is_vegan=dish.is_vegan,
            is_special=dish.is_special,
            toppings=[topping[0] for topping in await select_topping(dish.food_id)]
        )
        if dish.category_id not in category_dict:
            category_dict[dish.category_id] = DishResponseList(
                id=dish.category_id,
                name=dish.category_name,
                foods=[dish_model]
            )
        else:
            category_dict[dish.category_id].foods.append(dish_model)

    return [dish for dish in category_dict.values()]
