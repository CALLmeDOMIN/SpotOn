from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/recipes")
async def get_recipes(ingridients: str, numberofRecipes: int):
    external_api_url = "https://api.spoonacular.com/recipes/findByIngredients"
    try:
        response = requests.get(
            external_api_url,
            params={
                "ingredients": ingridients,
                "number": numberofRecipes,
                "apiKey": "YOUR_API"
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))
