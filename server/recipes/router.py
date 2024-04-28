import logging
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, Depends
from cachetools import TTLCache, cached
import os
import httpx
from .schema import RecipeQuery, RecipeNutrition

router = APIRouter()
load_dotenv()
logger = logging.getLogger("recipes")

cache_size = 100
cache_ttl = 300

recipes_cache = TTLCache(maxsize=cache_size, ttl=cache_ttl)
nutrition_cache = TTLCache(maxsize=cache_size, ttl=cache_ttl)


def get_api_key():
    return os.getenv("SPOONACULAR_API_KEY")


@router.get("/recipes")
@cached(cache=recipes_cache)
async def get_recipes(query: RecipeQuery, api_key: str = Depends(get_api_key)):
    # external_api_url = "https://api.spoonacular.com/recipes/findByIngredients"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                # external_api_url,
                params={
                    "apiKey": api_key,
                    "ingredients": query.ingredients,
                    "number": query.number_of_recipes,
                }
            )
            response.raise_for_status()

            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code,
                                detail=str(e))


@router.get("/recipes/{recipe_id}")
@cached(cache=nutrition_cache)
async def get_nutrition(query: RecipeNutrition, api_key: str = Depends(get_api_key)):
    external_api_url = (
        # f"https://api.spoonacular.com/recipes/{query.recipe_id}/information"
    )
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                # external_api_url,
                params={
                    "apiKey": api_key,
                    "includeNutrition": "true",
                }
            )

            response.raise_for_status()
            nutrition_data = response.json().get("nutrition", {}).get("nutrients", [])

            nutrients = {
                "carbohydrates": None,
                "protein": None,
                "calories": None
            }

            for nutrient in nutrition_data:
                if nutrient.get('name') in nutrients:
                    nutrients[nutrient.get('name').lower()
                              ] = nutrient.get('amount')

            return nutrients
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code,
                                detail=str(e))
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise HTTPException(
                status_code=500, detail="Internal Server Error")
