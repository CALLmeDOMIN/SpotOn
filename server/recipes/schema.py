from pydantic import BaseModel, Field


class RecipeQuery(BaseModel):
    ingredients: str = Field(..., example="tomatoes,flour",
                             description="A comma-separated list of ingredients")
    number_of_recipes: int = Field(
        gt=0, example=5, description="Number of recipes to return")


class RecipeNutrition(BaseModel):
    recipe_id: int = Field(..., example=12345,
                           description="The Spoonacular recipe ID")
