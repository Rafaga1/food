import asyncio
from typing import List

from sqlalchemy import select

from database import session
from models import food, food_category, topping, topping_food


async def get_dishes_list(topping_list=None, is_vegan=(1 == 1), is_special=(1 == 1)) -> List[tuple]:
    """
    Returns a list of dishes
    :param topping_list: Optional[List]
    :param is_vegan: Optional[bool]
    :param is_special: Optional[bool]
    :return: List[tuple]
    """
    if topping_list is not None:
        topping_condition = (topping.c.name.in_([item for item in topping_list]))
        topping_id_sub_query = (
            select(
                [
                    topping.c.id
                ]
            ).select_from(topping)
            .where(topping_condition)
        )

        topping_food_sub_query = (
            select(
                [
                    topping_food.c.food
                ]
            ).select_from(topping_food)
            .where(topping_food.c.topping.in_(topping_id_sub_query))
        )

    vegan_condition = (food.c.is_vegan == is_vegan)
    special_condition = (food.c.is_special == is_special)

    query = (
        select(
            [
                food_category.c.category_id,
                food_category.c.category_name,
                food.c.food_id,
                food.c.food_name,
                food.c.description,
                food.c.price,
                food.c.is_vegan,
                food.c.is_special,
            ]
        ).select_from(food.join(food_category))
        .where(food.c.is_publish == True, vegan_condition, special_condition,
               food.c.food_id.in_(topping_food_sub_query) if topping_list is not None else 1 == 1)

    )
    async with session.begin() as ses:
        dishes_list = await ses.execute(query)
        dishes_list = dishes_list.all()
    return dishes_list


async def select_topping(food_id: int):
    """
    Returns a list of toppings present in the dish.
    :param food_id: int
    :return: List[str]
    """
    sub_query = (
        select(
            [
                topping_food.c.topping
            ]
        ).select_from(topping_food)
        .where(topping_food.c.food == food_id)
    )
    query = (
        select(
            [
                topping.c.name
            ]
        ).select_from(topping)
        .filter(topping.c.id.in_(sub_query))
    )

    async with session.begin() as ses:
        topping_list = await ses.execute(query)
        topping_list = topping_list.all()
    return topping_list
