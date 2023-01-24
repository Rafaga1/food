
from fastapi import APIRouter, HTTPException, status

from utils.posts import like_post, dislike_post

from schemas import DishesRequest

router = APIRouter()



@router.get("/dish")
async def get_posts(dishes: DishesRequest):
    dishes_list = await post_utils.get_posts_count()
    posts = await post_utils.get_posts(page)
    return {"total_count": total_cout, "results": posts}