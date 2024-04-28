from pydantic import BaseModel


class RecipeQuery(BaseModel):
    ingredients: str
    numberOfRecipes: int

    class Config:
        json_schema_extra = {
            "example": {
                "ingredients": "apples,flour",
                "numberOfRecipes": 5,
            }
        }