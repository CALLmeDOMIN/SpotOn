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


@app.get("/")  # mock
def read_root():
    return [
        {
            "id": 640352,
            "title": "Cranberry Apple Crisp",
            "image": "https://img.spoonacular.com/recipes/640352-312x231.jpg",
            "imageType": "jpg",
            "usedIngredientCount": 1,
            "missedIngredientCount": 3,
            "missedIngredients": [
                {
                    "id": 9078,
                    "amount": 2.0,
                    "unit": "cups",
                    "unitLong": "cups",
                    "unitShort": "cup",
                    "aisle": "Produce",
                    "name": "cranberries",
                    "original": "2 cups fresh cranberries",
                    "originalName": "fresh cranberries",
                    "meta": [
                        "fresh"
                    ],
                    "extendedName": "fresh cranberries",
                    "image": "https://img.spoonacular.com/ingredients_100x100/cranberries.jpg"
                },
                {
                    "id": 1145,
                    "amount": 4.0,
                    "unit": "Tbs",
                    "unitLong": "Tbs",
                    "unitShort": "Tbs",
                    "aisle": "Milk, Eggs, Other Dairy",
                    "name": "butter",
                    "original": "1/2 stick (4 Tbs) unsalted butter, cut into cubes",
                    "originalName": "1/2 stick unsalted butter, cut into cubes",
                    "meta": [
                        "unsalted",
                        "cut into cubes"
                    ],
                    "extendedName": "unsalted butter",
                    "image": "https://img.spoonacular.com/ingredients_100x100/butter-sliced.jpg"
                },
                {
                    "id": 8120,
                    "amount": 1.5,
                    "unit": "cups",
                    "unitLong": "cups",
                    "unitShort": "cup",
                    "aisle": "Cereal",
                    "name": "regular oats",
                    "original": "1 1/2 cups regular oats (not quick-cooking)",
                    "originalName": "regular oats (not quick-cooking)",
                    "meta": [
                        "(not quick-cooking)"
                    ],
                    "image": "https://img.spoonacular.com/ingredients_100x100/rolled-oats.jpg"
                }
            ],
            "usedIngredients": [
                {
                    "id": 1089003,
                    "amount": 4.0,
                    "unit": "cups",
                    "unitLong": "cups",
                    "unitShort": "cup",
                    "aisle": "Produce",
                    "name": "granny smith apples",
                    "original": "4 cups Granny Smith apples, chopped into ½ inch chunks",
                    "originalName": "Granny Smith apples, chopped into ½ inch chunks",
                    "meta": [
                        "chopped"
                    ],
                    "image": "https://img.spoonacular.com/ingredients_100x100/grannysmith-apple.png"
                }
            ],
            "unusedIngredients": [],
            "likes": 11
        },
        {
            "id": 641803,
            "title": "Easy & Delish! ~ Apple Crumble",
            "image": "https://img.spoonacular.com/recipes/641803-312x231.jpg",
            "imageType": "jpg",
            "usedIngredientCount": 1,
            "missedIngredientCount": 3,
            "missedIngredients": [
                {
                    "id": 1001,
                    "amount": 0.75,
                    "unit": "stick",
                    "unitLong": "sticks",
                    "unitShort": "stick",
                    "aisle": "Milk, Eggs, Other Dairy",
                    "name": "butter",
                    "original": "3/4 stick of butter",
                    "originalName": "butter",
                    "meta": [],
                    "image": "https://img.spoonacular.com/ingredients_100x100/butter-sliced.jpg"
                },
                {
                    "id": 2011,
                    "amount": 1.0,
                    "unit": "Dash",
                    "unitLong": "Dash",
                    "unitShort": "Dash",
                    "aisle": "Spices and Seasonings",
                    "name": "ground cloves",
                    "original": "Dash of ground cloves",
                    "originalName": "ground cloves",
                    "meta": [],
                    "image": "https://img.spoonacular.com/ingredients_100x100/cloves.jpg"
                },
                {
                    "id": 9156,
                    "amount": 1.0,
                    "unit": "",
                    "unitLong": "",
                    "unitShort": "",
                    "aisle": "Produce",
                    "name": "lemon zest",
                    "original": "1 Zest of lemon",
                    "originalName": "Zest of lemon",
                    "meta": [],
                    "image": "https://img.spoonacular.com/ingredients_100x100/zest-lemon.jpg"
                }
            ],
            "usedIngredients": [
                {
                    "id": 9003,
                    "amount": 3.0,
                    "unit": "",
                    "unitLong": "",
                    "unitShort": "",
                    "aisle": "Produce",
                    "name": "apples",
                    "original": "3 apples – sliced",
                    "originalName": "apples – sliced",
                    "meta": [
                        "sliced"
                    ],
                    "image": "https://img.spoonacular.com/ingredients_100x100/apple.jpg"
                }
            ],
            "unusedIngredients": [],
            "likes": 1
        }
    ]


@app.get("/{recipe_id}")  # mock
def read_item(recipe_id: int):
    response = {
        "vegetarian": True,
        "vegan": False,
        "glutenFree": False,
        "dairyFree": False,
        "veryHealthy": False,
        "cheap": False,
        "veryPopular": False,
        "sustainable": False,
        "lowFodmap": False,
        "weightWatcherSmartPoints": 37,
        "gaps": "no",
        "preparationMinutes": -1,
        "cookingMinutes": -1,
        "aggregateLikes": 11,
        "healthScore": 3,
        "creditsText": "Foodista.com – The Cooking Encyclopedia Everyone Can Edit",
        "license": "CC BY 3.0",
        "sourceName": "Foodista",
        "pricePerServing": 153.59,
        "extendedIngredients": [
            {
                "id": 1089003,
                "aisle": "Produce",
                "image": "grannysmith-apple.png",
                "consistency": "SOLID",
                "name": "granny smith apples",
                "nameClean": "granny smith apple",
                "original": "4 cups Granny Smith apples, chopped into ½ inch chunks",
                "originalName": "Granny Smith apples, chopped into ½ inch chunks",
                "amount": 4.0,
                "unit": "cups",
                "meta": [
                    "chopped"
                ],
                "measures": {
                    "us": {
                        "amount": 4.0,
                        "unitShort": "cups",
                        "unitLong": "cups"
                    },
                    "metric": {
                        "amount": 500.0,
                        "unitShort": "g",
                        "unitLong": "grams"
                    }
                }
            },
            {
                "id": 9078,
                "aisle": "Produce",
                "image": "cranberries.jpg",
                "consistency": "SOLID",
                "name": "cranberries",
                "nameClean": "cranberries",
                "original": "2 cups fresh cranberries",
                "originalName": "fresh cranberries",
                "amount": 2.0,
                "unit": "cups",
                "meta": [
                    "fresh"
                ],
                "measures": {
                    "us": {
                        "amount": 2.0,
                        "unitShort": "cups",
                        "unitLong": "cups"
                    },
                    "metric": {
                        "amount": 200.0,
                        "unitShort": "g",
                        "unitLong": "grams"
                    }
                }
            },
            {
                "id": 19335,
                "aisle": "Baking",
                "image": "sugar-in-bowl.png",
                "consistency": "SOLID",
                "name": "sugar",
                "nameClean": "sugar",
                "original": "1 cup sugar",
                "originalName": "sugar",
                "amount": 1.0,
                "unit": "cup",
                "meta": [],
                "measures": {
                    "us": {
                        "amount": 1.0,
                        "unitShort": "cup",
                        "unitLong": "cup"
                    },
                    "metric": {
                        "amount": 200.0,
                        "unitShort": "g",
                        "unitLong": "grams"
                    }
                }
            },
            {
                "id": 1145,
                "aisle": "Milk, Eggs, Other Dairy",
                "image": "butter-sliced.jpg",
                "consistency": "SOLID",
                "name": "butter",
                "nameClean": "unsalted butter",
                "original": "1/2 stick (4 Tbs) unsalted butter, cut into cubes",
                "originalName": "1/2 stick unsalted butter, cut into cubes",
                "amount": 4.0,
                "unit": "Tbs",
                "meta": [
                    "unsalted",
                    "cut into cubes"
                ],
                "measures": {
                    "us": {
                        "amount": 4.0,
                        "unitShort": "Tbs",
                        "unitLong": "Tbs"
                    },
                    "metric": {
                        "amount": 4.0,
                        "unitShort": "Tbs",
                        "unitLong": "Tbs"
                    }
                }
            },
            {
                "id": 8120,
                "aisle": "Cereal",
                "image": "rolled-oats.jpg",
                "consistency": "SOLID",
                "name": "regular oats",
                "nameClean": "rolled oats",
                "original": "1 1/2 cups regular oats (not quick-cooking)",
                "originalName": "regular oats (not quick-cooking)",
                "amount": 1.5,
                "unit": "cups",
                "meta": [
                    "(not quick-cooking)"
                ],
                "measures": {
                    "us": {
                        "amount": 1.5,
                        "unitShort": "cups",
                        "unitLong": "cups"
                    },
                    "metric": {
                        "amount": 121.622,
                        "unitShort": "g",
                        "unitLong": "grams"
                    }
                }
            },
            {
                "id": 19334,
                "aisle": "Baking",
                "image": "light-brown-sugar.jpg",
                "consistency": "SOLID",
                "name": "brown sugar",
                "nameClean": "golden brown sugar",
                "original": "1/2 cup light brown sugar",
                "originalName": "light brown sugar",
                "amount": 0.5,
                "unit": "cup",
                "meta": [
                    "light"
                ],
                "measures": {
                    "us": {
                        "amount": 0.5,
                        "unitShort": "cups",
                        "unitLong": "cups"
                    },
                    "metric": {
                        "amount": 110.0,
                        "unitShort": "g",
                        "unitLong": "grams"
                    }
                }
            },
            {
                "id": 19334,
                "aisle": "Baking",
                "image": "dark-brown-sugar.png",
                "consistency": "SOLID",
                "name": "brown sugar",
                "nameClean": "golden brown sugar",
                "original": "1/2 cup light brown sugar",
                "originalName": "light brown sugar",
                "amount": 0.5,
                "unit": "cup",
                "meta": [
                    "light"
                ],
                "measures": {
                    "us": {
                        "amount": 0.5,
                        "unitShort": "cups",
                        "unitLong": "cups"
                    },
                    "metric": {
                        "amount": 110.0,
                        "unitShort": "g",
                        "unitLong": "grams"
                    }
                }
            },
            {
                "id": 20081,
                "aisle": "Baking",
                "image": "flour.png",
                "consistency": "SOLID",
                "name": "flour",
                "nameClean": "wheat flour",
                "original": "1/4 cup all-purpose flour",
                "originalName": "all-purpose flour",
                "amount": 0.25,
                "unit": "cup",
                "meta": [
                    "all-purpose"
                ],
                "measures": {
                    "us": {
                        "amount": 0.25,
                        "unitShort": "cups",
                        "unitLong": "cups"
                    },
                    "metric": {
                        "amount": 31.25,
                        "unitShort": "g",
                        "unitLong": "grams"
                    }
                }
            },
            {
                "id": 1145,
                "aisle": "Milk, Eggs, Other Dairy",
                "image": "butter-sliced.jpg",
                "consistency": "SOLID",
                "name": "butter",
                "nameClean": "unsalted butter",
                "original": "1 stick unsalted butter, melted",
                "originalName": "unsalted butter, melted",
                "amount": 1.0,
                "unit": "stick",
                "meta": [
                    "unsalted",
                    "melted"
                ],
                "measures": {
                    "us": {
                        "amount": 1.0,
                        "unitShort": "stick",
                        "unitLong": "stick"
                    },
                    "metric": {
                        "amount": 1.0,
                        "unitShort": "stick",
                        "unitLong": "stick"
                    }
                }
            }
        ],
        "id": 640352,
        "title": "Cranberry Apple Crisp",
        "readyInMinutes": 45,
        "servings": 4,
        "sourceUrl": "https://www.foodista.com/recipe/TJXDHDFD/cranberry-apple-crisp",
        "image": "https://img.spoonacular.com/recipes/640352-556x370.jpg",
        "imageType": "jpg",
        "nutrition": {
            "nutrients": [
                {
                    "name": "Calories",
                    "amount": 937.54,
                    "unit": "kcal",
                    "percentOfDailyNeeds": 46.88
                },
                {
                    "name": "Fat",
                    "amount": 36.93,
                    "unit": "g",
                    "percentOfDailyNeeds": 56.81
                },
                {
                    "name": "Saturated Fat",
                    "amount": 22.19,
                    "unit": "g",
                    "percentOfDailyNeeds": 138.71
                },
                {
                    "name": "Carbohydrates",
                    "amount": 153.58,
                    "unit": "g",
                    "percentOfDailyNeeds": 51.19
                },
                {
                    "name": "Net Carbohydrates",
                    "amount": 145.49,
                    "unit": "g",
                    "percentOfDailyNeeds": 52.91
                },
                {
                    "name": "Sugar",
                    "amount": 118.73,
                    "unit": "g",
                    "percentOfDailyNeeds": 131.93
                },
                {
                    "name": "Cholesterol",
                    "amount": 91.27,
                    "unit": "mg",
                    "percentOfDailyNeeds": 30.42
                },
                {
                    "name": "Sodium",
                    "amount": 24.8,
                    "unit": "mg",
                    "percentOfDailyNeeds": 1.08
                },
                {
                    "name": "Protein",
                    "amount": 5.8,
                    "unit": "g",
                    "percentOfDailyNeeds": 11.6
                },
                {
                    "name": "Manganese",
                    "amount": 1.42,
                    "unit": "mg",
                    "percentOfDailyNeeds": 70.98
                },
                {
                    "name": "Fiber",
                    "amount": 8.08,
                    "unit": "g",
                    "percentOfDailyNeeds": 32.33
                },
                {
                    "name": "Vitamin A",
                    "amount": 1158.33,
                    "unit": "IU",
                    "percentOfDailyNeeds": 23.17
                },
                {
                    "name": "Selenium",
                    "amount": 12.87,
                    "unit": "µg",
                    "percentOfDailyNeeds": 18.39
                },
                {
                    "name": "Phosphorus",
                    "amount": 164.74,
                    "unit": "mg",
                    "percentOfDailyNeeds": 16.47
                },
                {
                    "name": "Vitamin C",
                    "amount": 12.75,
                    "unit": "mg",
                    "percentOfDailyNeeds": 15.45
                },
                {
                    "name": "Vitamin B1",
                    "amount": 0.23,
                    "unit": "mg",
                    "percentOfDailyNeeds": 15.37
                },
                {
                    "name": "Magnesium",
                    "amount": 58.73,
                    "unit": "mg",
                    "percentOfDailyNeeds": 14.68
                },
                {
                    "name": "Vitamin E",
                    "amount": 2.0,
                    "unit": "mg",
                    "percentOfDailyNeeds": 13.35
                },
                {
                    "name": "Iron",
                    "amount": 2.34,
                    "unit": "mg",
                    "percentOfDailyNeeds": 13.02
                },
                {
                    "name": "Copper",
                    "amount": 0.23,
                    "unit": "mg",
                    "percentOfDailyNeeds": 11.4
                },
                {
                    "name": "Potassium",
                    "amount": 376.52,
                    "unit": "mg",
                    "percentOfDailyNeeds": 10.76
                },
                {
                    "name": "Vitamin B2",
                    "amount": 0.15,
                    "unit": "mg",
                    "percentOfDailyNeeds": 8.95
                },
                {
                    "name": "Zinc",
                    "amount": 1.32,
                    "unit": "mg",
                    "percentOfDailyNeeds": 8.77
                },
                {
                    "name": "Calcium",
                    "amount": 84.82,
                    "unit": "mg",
                    "percentOfDailyNeeds": 8.48
                },
                {
                    "name": "Vitamin K",
                    "amount": 8.85,
                    "unit": "µg",
                    "percentOfDailyNeeds": 8.43
                },
                {
                    "name": "Folate",
                    "amount": 30.1,
                    "unit": "µg",
                    "percentOfDailyNeeds": 7.53
                },
                {
                    "name": "Vitamin B5",
                    "amount": 0.72,
                    "unit": "mg",
                    "percentOfDailyNeeds": 7.18
                },
                {
                    "name": "Vitamin B6",
                    "amount": 0.14,
                    "unit": "mg",
                    "percentOfDailyNeeds": 6.87
                },
                {
                    "name": "Vitamin B3",
                    "amount": 1.04,
                    "unit": "mg",
                    "percentOfDailyNeeds": 5.22
                },
                {
                    "name": "Vitamin D",
                    "amount": 0.64,
                    "unit": "µg",
                    "percentOfDailyNeeds": 4.24
                },
                {
                    "name": "Vitamin B12",
                    "amount": 0.07,
                    "unit": "µg",
                    "percentOfDailyNeeds": 1.2
                }
            ],
            "properties": [
                {
                    "name": "Glycemic Index",
                    "amount": 65.52,
                    "unit": ""
                },
                {
                    "name": "Glycemic Load",
                    "amount": 52.67,
                    "unit": ""
                },
                {
                    "name": "Inflammation Score",
                    "amount": -7.0,
                    "unit": ""
                },
                {
                    "name": "Nutrition Score",
                    "amount": 14.010434782608696,
                    "unit": "%"
                }
            ],
            "flavonoids": [
                {
                    "name": "Cyanidin",
                    "amount": 25.18,
                    "unit": "mg"
                },
                {
                    "name": "Petunidin",
                    "amount": 0.0,
                    "unit": "mg"
                },
                {
                    "name": "Delphinidin",
                    "amount": 3.84,
                    "unit": "mg"
                },
                {
                    "name": "Malvidin",
                    "amount": 0.22,
                    "unit": "mg"
                },
                {
                    "name": "Pelargonidin",
                    "amount": 0.16,
                    "unit": "mg"
                },
                {
                    "name": "Peonidin",
                    "amount": 24.61,
                    "unit": "mg"
                },
                {
                    "name": "Catechin",
                    "amount": 1.82,
                    "unit": "mg"
                },
                {
                    "name": "Epigallocatechin",
                    "amount": 0.7,
                    "unit": "mg"
                },
                {
                    "name": "Epicatechin",
                    "amount": 11.6,
                    "unit": "mg"
                },
                {
                    "name": "Epicatechin 3-gallate",
                    "amount": 0.01,
                    "unit": "mg"
                },
                {
                    "name": "Epigallocatechin 3-gallate",
                    "amount": 0.72,
                    "unit": "mg"
                },
                {
                    "name": "Theaflavin",
                    "amount": 0.0,
                    "unit": ""
                },
                {
                    "name": "Thearubigins",
                    "amount": 0.0,
                    "unit": ""
                },
                {
                    "name": "Eriodictyol",
                    "amount": 0.0,
                    "unit": ""
                },
                {
                    "name": "Hesperetin",
                    "amount": 0.0,
                    "unit": "mg"
                },
                {
                    "name": "Naringenin",
                    "amount": 0.0,
                    "unit": "mg"
                },
                {
                    "name": "Apigenin",
                    "amount": 0.0,
                    "unit": "mg"
                },
                {
                    "name": "Luteolin",
                    "amount": 0.15,
                    "unit": "mg"
                },
                {
                    "name": "Isorhamnetin",
                    "amount": 0.0,
                    "unit": ""
                },
                {
                    "name": "Kaempferol",
                    "amount": 0.24,
                    "unit": "mg"
                },
                {
                    "name": "Myricetin",
                    "amount": 3.32,
                    "unit": "mg"
                },
                {
                    "name": "Quercetin",
                    "amount": 12.43,
                    "unit": "mg"
                },
                {
                    "name": "Theaflavin-3,3'-digallate",
                    "amount": 0.0,
                    "unit": ""
                },
                {
                    "name": "Theaflavin-3'-gallate",
                    "amount": 0.0,
                    "unit": ""
                },
                {
                    "name": "Theaflavin-3-gallate",
                    "amount": 0.0,
                    "unit": ""
                },
                {
                    "name": "Gallocatechin",
                    "amount": 0.0,
                    "unit": "mg"
                }
            ],
            "ingredients": [
                {
                    "id": 1089003,
                    "name": "granny smith apples",
                    "amount": 1.0,
                    "unit": "cups",
                    "nutrients": [
                        {
                            "name": "Protein",
                            "amount": 0.32,
                            "unit": "g",
                            "percentOfDailyNeeds": 11.6
                        },
                        {
                            "name": "Copper",
                            "amount": 0.03,
                            "unit": "mg",
                            "percentOfDailyNeeds": 11.4
                        },
                        {
                            "name": "Iron",
                            "amount": 0.15,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.02
                        },
                        {
                            "name": "Potassium",
                            "amount": 133.75,
                            "unit": "mg",
                            "percentOfDailyNeeds": 10.76
                        },
                        {
                            "name": "Calories",
                            "amount": 65.0,
                            "unit": "kcal",
                            "percentOfDailyNeeds": 46.88
                        },
                        {
                            "name": "Net Carbohydrates",
                            "amount": 14.25,
                            "unit": "g",
                            "percentOfDailyNeeds": 52.91
                        },
                        {
                            "name": "Saturated Fat",
                            "amount": 0.04,
                            "unit": "g",
                            "percentOfDailyNeeds": 138.71
                        },
                        {
                            "name": "Vitamin B12",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 1.2
                        },
                        {
                            "name": "Vitamin B2",
                            "amount": 0.03,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.95
                        },
                        {
                            "name": "Vitamin A",
                            "amount": 67.5,
                            "unit": "IU",
                            "percentOfDailyNeeds": 23.17
                        },
                        {
                            "name": "Fiber",
                            "amount": 3.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 32.33
                        },
                        {
                            "name": "Vitamin B3",
                            "amount": 0.11,
                            "unit": "mg",
                            "percentOfDailyNeeds": 5.22
                        },
                        {
                            "name": "Poly Unsaturated Fat",
                            "amount": 0.06,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Phosphorus",
                            "amount": 13.75,
                            "unit": "mg",
                            "percentOfDailyNeeds": 16.47
                        },
                        {
                            "name": "Fluoride",
                            "amount": 4.13,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin E",
                            "amount": 0.22,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.35
                        },
                        {
                            "name": "Zinc",
                            "amount": 0.05,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.77
                        },
                        {
                            "name": "Mono Unsaturated Fat",
                            "amount": 0.01,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Alcohol",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B1",
                            "amount": 0.02,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.37
                        },
                        {
                            "name": "Cholesterol",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 30.42
                        },
                        {
                            "name": "Selenium",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 18.39
                        },
                        {
                            "name": "Folic Acid",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Lycopene",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Folate",
                            "amount": 3.75,
                            "unit": "µg",
                            "percentOfDailyNeeds": 7.53
                        },
                        {
                            "name": "Choline",
                            "amount": 4.25,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B5",
                            "amount": 0.08,
                            "unit": "mg",
                            "percentOfDailyNeeds": 7.18
                        },
                        {
                            "name": "Vitamin D",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 4.24
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 17.25,
                            "unit": "g",
                            "percentOfDailyNeeds": 51.19
                        },
                        {
                            "name": "Vitamin B6",
                            "amount": 0.05,
                            "unit": "mg",
                            "percentOfDailyNeeds": 6.87
                        },
                        {
                            "name": "Sugar",
                            "amount": 13.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 131.93
                        },
                        {
                            "name": "Caffeine",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Manganese",
                            "amount": 0.04,
                            "unit": "mg",
                            "percentOfDailyNeeds": 70.98
                        },
                        {
                            "name": "Magnesium",
                            "amount": 6.25,
                            "unit": "mg",
                            "percentOfDailyNeeds": 14.68
                        },
                        {
                            "name": "Sodium",
                            "amount": 1.25,
                            "unit": "mg",
                            "percentOfDailyNeeds": 1.08
                        },
                        {
                            "name": "Fat",
                            "amount": 0.21,
                            "unit": "g",
                            "percentOfDailyNeeds": 56.81
                        },
                        {
                            "name": "Vitamin C",
                            "amount": 5.75,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.45
                        },
                        {
                            "name": "Vitamin K",
                            "amount": 2.75,
                            "unit": "µg",
                            "percentOfDailyNeeds": 8.43
                        },
                        {
                            "name": "Calcium",
                            "amount": 7.5,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.48
                        }
                    ]
                },
                {
                    "id": 9078,
                    "name": "cranberries",
                    "amount": 0.5,
                    "unit": "cups",
                    "nutrients": [
                        {
                            "name": "Protein",
                            "amount": 0.23,
                            "unit": "g",
                            "percentOfDailyNeeds": 11.6
                        },
                        {
                            "name": "Copper",
                            "amount": 0.03,
                            "unit": "mg",
                            "percentOfDailyNeeds": 11.4
                        },
                        {
                            "name": "Iron",
                            "amount": 0.12,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.02
                        },
                        {
                            "name": "Potassium",
                            "amount": 40.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 10.76
                        },
                        {
                            "name": "Calories",
                            "amount": 23.0,
                            "unit": "kcal",
                            "percentOfDailyNeeds": 46.88
                        },
                        {
                            "name": "Net Carbohydrates",
                            "amount": 4.2,
                            "unit": "g",
                            "percentOfDailyNeeds": 52.91
                        },
                        {
                            "name": "Saturated Fat",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 138.71
                        },
                        {
                            "name": "Vitamin B12",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 1.2
                        },
                        {
                            "name": "Fiber",
                            "amount": 1.8,
                            "unit": "g",
                            "percentOfDailyNeeds": 32.33
                        },
                        {
                            "name": "Vitamin A",
                            "amount": 30.0,
                            "unit": "IU",
                            "percentOfDailyNeeds": 23.17
                        },
                        {
                            "name": "Vitamin B2",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.95
                        },
                        {
                            "name": "Vitamin B3",
                            "amount": 0.05,
                            "unit": "mg",
                            "percentOfDailyNeeds": 5.22
                        },
                        {
                            "name": "Poly Unsaturated Fat",
                            "amount": 0.03,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Phosphorus",
                            "amount": 5.5,
                            "unit": "mg",
                            "percentOfDailyNeeds": 16.47
                        },
                        {
                            "name": "Vitamin E",
                            "amount": 0.66,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.35
                        },
                        {
                            "name": "Zinc",
                            "amount": 0.05,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.77
                        },
                        {
                            "name": "Mono Unsaturated Fat",
                            "amount": 0.01,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Alcohol",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B1",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.37
                        },
                        {
                            "name": "Cholesterol",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 30.42
                        },
                        {
                            "name": "Selenium",
                            "amount": 0.05,
                            "unit": "µg",
                            "percentOfDailyNeeds": 18.39
                        },
                        {
                            "name": "Folic Acid",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Lycopene",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Folate",
                            "amount": 0.5,
                            "unit": "µg",
                            "percentOfDailyNeeds": 7.53
                        },
                        {
                            "name": "Choline",
                            "amount": 2.75,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B5",
                            "amount": 0.15,
                            "unit": "mg",
                            "percentOfDailyNeeds": 7.18
                        },
                        {
                            "name": "Vitamin D",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 4.24
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 6.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 51.19
                        },
                        {
                            "name": "Vitamin B6",
                            "amount": 0.03,
                            "unit": "mg",
                            "percentOfDailyNeeds": 6.87
                        },
                        {
                            "name": "Sugar",
                            "amount": 2.13,
                            "unit": "g",
                            "percentOfDailyNeeds": 131.93
                        },
                        {
                            "name": "Caffeine",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Manganese",
                            "amount": 0.18,
                            "unit": "mg",
                            "percentOfDailyNeeds": 70.98
                        },
                        {
                            "name": "Magnesium",
                            "amount": 3.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 14.68
                        },
                        {
                            "name": "Sodium",
                            "amount": 1.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 1.08
                        },
                        {
                            "name": "Fat",
                            "amount": 0.06,
                            "unit": "g",
                            "percentOfDailyNeeds": 56.81
                        },
                        {
                            "name": "Vitamin C",
                            "amount": 7.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.45
                        },
                        {
                            "name": "Vitamin K",
                            "amount": 2.5,
                            "unit": "µg",
                            "percentOfDailyNeeds": 8.43
                        },
                        {
                            "name": "Calcium",
                            "amount": 4.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.48
                        }
                    ]
                },
                {
                    "id": 19335,
                    "name": "sugar",
                    "amount": 0.25,
                    "unit": "cup",
                    "nutrients": [
                        {
                            "name": "Protein",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 11.6
                        },
                        {
                            "name": "Copper",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 11.4
                        },
                        {
                            "name": "Iron",
                            "amount": 0.03,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.02
                        },
                        {
                            "name": "Potassium",
                            "amount": 1.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 10.76
                        },
                        {
                            "name": "Calories",
                            "amount": 192.5,
                            "unit": "kcal",
                            "percentOfDailyNeeds": 46.88
                        },
                        {
                            "name": "Net Carbohydrates",
                            "amount": 49.8,
                            "unit": "g",
                            "percentOfDailyNeeds": 52.91
                        },
                        {
                            "name": "Saturated Fat",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 138.71
                        },
                        {
                            "name": "Vitamin B12",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 1.2
                        },
                        {
                            "name": "Vitamin B2",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.95
                        },
                        {
                            "name": "Vitamin A",
                            "amount": 0.0,
                            "unit": "IU",
                            "percentOfDailyNeeds": 23.17
                        },
                        {
                            "name": "Fiber",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 32.33
                        },
                        {
                            "name": "Vitamin B3",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 5.22
                        },
                        {
                            "name": "Poly Unsaturated Fat",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Phosphorus",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 16.47
                        },
                        {
                            "name": "Fluoride",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin E",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.35
                        },
                        {
                            "name": "Zinc",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.77
                        },
                        {
                            "name": "Mono Unsaturated Fat",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Alcohol",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B1",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.37
                        },
                        {
                            "name": "Cholesterol",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 30.42
                        },
                        {
                            "name": "Selenium",
                            "amount": 0.3,
                            "unit": "µg",
                            "percentOfDailyNeeds": 18.39
                        },
                        {
                            "name": "Folic Acid",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Lycopene",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Folate",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 7.53
                        },
                        {
                            "name": "Choline",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B5",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 7.18
                        },
                        {
                            "name": "Vitamin D",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 4.24
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 49.8,
                            "unit": "g",
                            "percentOfDailyNeeds": 51.19
                        },
                        {
                            "name": "Vitamin B6",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 6.87
                        },
                        {
                            "name": "Sugar",
                            "amount": 49.9,
                            "unit": "g",
                            "percentOfDailyNeeds": 131.93
                        },
                        {
                            "name": "Caffeine",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Manganese",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 70.98
                        },
                        {
                            "name": "Magnesium",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 14.68
                        },
                        {
                            "name": "Sodium",
                            "amount": 0.5,
                            "unit": "mg",
                            "percentOfDailyNeeds": 1.08
                        },
                        {
                            "name": "Fat",
                            "amount": 0.16,
                            "unit": "g",
                            "percentOfDailyNeeds": 56.81
                        },
                        {
                            "name": "Vitamin C",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.45
                        },
                        {
                            "name": "Vitamin K",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 8.43
                        },
                        {
                            "name": "Calcium",
                            "amount": 0.5,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.48
                        }
                    ]
                },
                {
                    "id": 1145,
                    "name": "butter",
                    "amount": 1.0,
                    "unit": "Tbs",
                    "nutrients": [
                        {
                            "name": "Protein",
                            "amount": 0.12,
                            "unit": "g",
                            "percentOfDailyNeeds": 11.6
                        },
                        {
                            "name": "Copper",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 11.4
                        },
                        {
                            "name": "Iron",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.02
                        },
                        {
                            "name": "Potassium",
                            "amount": 3.41,
                            "unit": "mg",
                            "percentOfDailyNeeds": 10.76
                        },
                        {
                            "name": "Calories",
                            "amount": 101.81,
                            "unit": "kcal",
                            "percentOfDailyNeeds": 46.88
                        },
                        {
                            "name": "Net Carbohydrates",
                            "amount": 0.01,
                            "unit": "g",
                            "percentOfDailyNeeds": 52.91
                        },
                        {
                            "name": "Saturated Fat",
                            "amount": 7.29,
                            "unit": "g",
                            "percentOfDailyNeeds": 138.71
                        },
                        {
                            "name": "Vitamin B12",
                            "amount": 0.02,
                            "unit": "µg",
                            "percentOfDailyNeeds": 1.2
                        },
                        {
                            "name": "Vitamin B2",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.95
                        },
                        {
                            "name": "Vitamin A",
                            "amount": 354.86,
                            "unit": "IU",
                            "percentOfDailyNeeds": 23.17
                        },
                        {
                            "name": "Fiber",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 32.33
                        },
                        {
                            "name": "Vitamin B3",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 5.22
                        },
                        {
                            "name": "Poly Unsaturated Fat",
                            "amount": 0.43,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Phosphorus",
                            "amount": 3.41,
                            "unit": "mg",
                            "percentOfDailyNeeds": 16.47
                        },
                        {
                            "name": "Fluoride",
                            "amount": 0.4,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin E",
                            "amount": 0.33,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.35
                        },
                        {
                            "name": "Zinc",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.77
                        },
                        {
                            "name": "Mono Unsaturated Fat",
                            "amount": 2.98,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Trans Fat",
                            "amount": 0.47,
                            "unit": "g",
                            "percentOfDailyNeeds": 13915.11
                        },
                        {
                            "name": "Alcohol",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B1",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.37
                        },
                        {
                            "name": "Cholesterol",
                            "amount": 30.53,
                            "unit": "mg",
                            "percentOfDailyNeeds": 30.42
                        },
                        {
                            "name": "Selenium",
                            "amount": 0.14,
                            "unit": "µg",
                            "percentOfDailyNeeds": 18.39
                        },
                        {
                            "name": "Folic Acid",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Lycopene",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Folate",
                            "amount": 0.43,
                            "unit": "µg",
                            "percentOfDailyNeeds": 7.53
                        },
                        {
                            "name": "Choline",
                            "amount": 2.67,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B5",
                            "amount": 0.02,
                            "unit": "mg",
                            "percentOfDailyNeeds": 7.18
                        },
                        {
                            "name": "Vitamin D",
                            "amount": 0.21,
                            "unit": "µg",
                            "percentOfDailyNeeds": 4.24
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 0.01,
                            "unit": "g",
                            "percentOfDailyNeeds": 51.19
                        },
                        {
                            "name": "Vitamin B6",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 6.87
                        },
                        {
                            "name": "Sugar",
                            "amount": 0.01,
                            "unit": "g",
                            "percentOfDailyNeeds": 131.93
                        },
                        {
                            "name": "Caffeine",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Manganese",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 70.98
                        },
                        {
                            "name": "Magnesium",
                            "amount": 0.28,
                            "unit": "mg",
                            "percentOfDailyNeeds": 14.68
                        },
                        {
                            "name": "Sodium",
                            "amount": 1.56,
                            "unit": "mg",
                            "percentOfDailyNeeds": 1.08
                        },
                        {
                            "name": "Fat",
                            "amount": 11.52,
                            "unit": "g",
                            "percentOfDailyNeeds": 56.81
                        },
                        {
                            "name": "Vitamin C",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.45
                        },
                        {
                            "name": "Vitamin K",
                            "amount": 0.99,
                            "unit": "µg",
                            "percentOfDailyNeeds": 8.43
                        },
                        {
                            "name": "Calcium",
                            "amount": 3.41,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.48
                        }
                    ]
                },
                {
                    "id": 8120,
                    "name": "regular oats",
                    "amount": 0.38,
                    "unit": "cups",
                    "nutrients": [
                        {
                            "name": "Protein",
                            "amount": 4.01,
                            "unit": "g",
                            "percentOfDailyNeeds": 11.6
                        },
                        {
                            "name": "Copper",
                            "amount": 0.12,
                            "unit": "mg",
                            "percentOfDailyNeeds": 11.4
                        },
                        {
                            "name": "Iron",
                            "amount": 1.29,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.02
                        },
                        {
                            "name": "Potassium",
                            "amount": 110.07,
                            "unit": "mg",
                            "percentOfDailyNeeds": 10.76
                        },
                        {
                            "name": "Calories",
                            "amount": 115.24,
                            "unit": "kcal",
                            "percentOfDailyNeeds": 46.88
                        },
                        {
                            "name": "Net Carbohydrates",
                            "amount": 17.51,
                            "unit": "g",
                            "percentOfDailyNeeds": 52.91
                        },
                        {
                            "name": "Saturated Fat",
                            "amount": 0.34,
                            "unit": "g",
                            "percentOfDailyNeeds": 138.71
                        },
                        {
                            "name": "Vitamin B12",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 1.2
                        },
                        {
                            "name": "Fiber",
                            "amount": 3.07,
                            "unit": "g",
                            "percentOfDailyNeeds": 32.33
                        },
                        {
                            "name": "Vitamin A",
                            "amount": 0.0,
                            "unit": "IU",
                            "percentOfDailyNeeds": 23.17
                        },
                        {
                            "name": "Vitamin B2",
                            "amount": 0.05,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.95
                        },
                        {
                            "name": "Vitamin B3",
                            "amount": 0.34,
                            "unit": "mg",
                            "percentOfDailyNeeds": 5.22
                        },
                        {
                            "name": "Poly Unsaturated Fat",
                            "amount": 0.7,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Phosphorus",
                            "amount": 124.66,
                            "unit": "mg",
                            "percentOfDailyNeeds": 16.47
                        },
                        {
                            "name": "Vitamin E",
                            "amount": 0.13,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.35
                        },
                        {
                            "name": "Zinc",
                            "amount": 1.11,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.77
                        },
                        {
                            "name": "Mono Unsaturated Fat",
                            "amount": 0.6,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Alcohol",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B1",
                            "amount": 0.14,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.37
                        },
                        {
                            "name": "Cholesterol",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 30.42
                        },
                        {
                            "name": "Selenium",
                            "amount": 8.79,
                            "unit": "µg",
                            "percentOfDailyNeeds": 18.39
                        },
                        {
                            "name": "Folic Acid",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Lycopene",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Folate",
                            "amount": 9.73,
                            "unit": "µg",
                            "percentOfDailyNeeds": 7.53
                        },
                        {
                            "name": "Choline",
                            "amount": 12.28,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B5",
                            "amount": 0.34,
                            "unit": "mg",
                            "percentOfDailyNeeds": 7.18
                        },
                        {
                            "name": "Vitamin D",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 4.24
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 20.58,
                            "unit": "g",
                            "percentOfDailyNeeds": 51.19
                        },
                        {
                            "name": "Vitamin B6",
                            "amount": 0.03,
                            "unit": "mg",
                            "percentOfDailyNeeds": 6.87
                        },
                        {
                            "name": "Sugar",
                            "amount": 0.3,
                            "unit": "g",
                            "percentOfDailyNeeds": 131.93
                        },
                        {
                            "name": "Caffeine",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Manganese",
                            "amount": 1.1,
                            "unit": "mg",
                            "percentOfDailyNeeds": 70.98
                        },
                        {
                            "name": "Magnesium",
                            "amount": 41.96,
                            "unit": "mg",
                            "percentOfDailyNeeds": 14.68
                        },
                        {
                            "name": "Sodium",
                            "amount": 1.82,
                            "unit": "mg",
                            "percentOfDailyNeeds": 1.08
                        },
                        {
                            "name": "Fat",
                            "amount": 1.98,
                            "unit": "g",
                            "percentOfDailyNeeds": 56.81
                        },
                        {
                            "name": "Vitamin C",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.45
                        },
                        {
                            "name": "Vitamin K",
                            "amount": 0.61,
                            "unit": "µg",
                            "percentOfDailyNeeds": 8.43
                        },
                        {
                            "name": "Calcium",
                            "amount": 15.81,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.48
                        }
                    ]
                },
                {
                    "id": 19334,
                    "name": "brown sugar",
                    "amount": 0.13,
                    "unit": "cup",
                    "nutrients": [
                        {
                            "name": "Protein",
                            "amount": 0.03,
                            "unit": "g",
                            "percentOfDailyNeeds": 11.6
                        },
                        {
                            "name": "Copper",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 11.4
                        },
                        {
                            "name": "Iron",
                            "amount": 0.2,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.02
                        },
                        {
                            "name": "Potassium",
                            "amount": 36.58,
                            "unit": "mg",
                            "percentOfDailyNeeds": 10.76
                        },
                        {
                            "name": "Calories",
                            "amount": 104.5,
                            "unit": "kcal",
                            "percentOfDailyNeeds": 46.88
                        },
                        {
                            "name": "Net Carbohydrates",
                            "amount": 26.98,
                            "unit": "g",
                            "percentOfDailyNeeds": 52.91
                        },
                        {
                            "name": "Saturated Fat",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 138.71
                        },
                        {
                            "name": "Vitamin B12",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 1.2
                        },
                        {
                            "name": "Fiber",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 32.33
                        },
                        {
                            "name": "Vitamin A",
                            "amount": 0.0,
                            "unit": "IU",
                            "percentOfDailyNeeds": 23.17
                        },
                        {
                            "name": "Vitamin B2",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.95
                        },
                        {
                            "name": "Vitamin B3",
                            "amount": 0.03,
                            "unit": "mg",
                            "percentOfDailyNeeds": 5.22
                        },
                        {
                            "name": "Poly Unsaturated Fat",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Phosphorus",
                            "amount": 1.1,
                            "unit": "mg",
                            "percentOfDailyNeeds": 16.47
                        },
                        {
                            "name": "Vitamin E",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.35
                        },
                        {
                            "name": "Zinc",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.77
                        },
                        {
                            "name": "Mono Unsaturated Fat",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Alcohol",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B1",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.37
                        },
                        {
                            "name": "Cholesterol",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 30.42
                        },
                        {
                            "name": "Selenium",
                            "amount": 0.33,
                            "unit": "µg",
                            "percentOfDailyNeeds": 18.39
                        },
                        {
                            "name": "Folic Acid",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Lycopene",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Folate",
                            "amount": 0.28,
                            "unit": "µg",
                            "percentOfDailyNeeds": 7.53
                        },
                        {
                            "name": "Choline",
                            "amount": 0.63,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B5",
                            "amount": 0.04,
                            "unit": "mg",
                            "percentOfDailyNeeds": 7.18
                        },
                        {
                            "name": "Vitamin D",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 4.24
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 26.98,
                            "unit": "g",
                            "percentOfDailyNeeds": 51.19
                        },
                        {
                            "name": "Vitamin B6",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 6.87
                        },
                        {
                            "name": "Sugar",
                            "amount": 26.67,
                            "unit": "g",
                            "percentOfDailyNeeds": 131.93
                        },
                        {
                            "name": "Caffeine",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Manganese",
                            "amount": 0.02,
                            "unit": "mg",
                            "percentOfDailyNeeds": 70.98
                        },
                        {
                            "name": "Magnesium",
                            "amount": 2.47,
                            "unit": "mg",
                            "percentOfDailyNeeds": 14.68
                        },
                        {
                            "name": "Sodium",
                            "amount": 7.7,
                            "unit": "mg",
                            "percentOfDailyNeeds": 1.08
                        },
                        {
                            "name": "Fat",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 56.81
                        },
                        {
                            "name": "Vitamin C",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.45
                        },
                        {
                            "name": "Vitamin K",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 8.43
                        },
                        {
                            "name": "Calcium",
                            "amount": 22.83,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.48
                        }
                    ]
                },
                {
                    "id": 19334,
                    "name": "brown sugar",
                    "amount": 0.13,
                    "unit": "cup",
                    "nutrients": [
                        {
                            "name": "Protein",
                            "amount": 0.03,
                            "unit": "g",
                            "percentOfDailyNeeds": 11.6
                        },
                        {
                            "name": "Copper",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 11.4
                        },
                        {
                            "name": "Iron",
                            "amount": 0.2,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.02
                        },
                        {
                            "name": "Potassium",
                            "amount": 36.58,
                            "unit": "mg",
                            "percentOfDailyNeeds": 10.76
                        },
                        {
                            "name": "Calories",
                            "amount": 104.5,
                            "unit": "kcal",
                            "percentOfDailyNeeds": 46.88
                        },
                        {
                            "name": "Net Carbohydrates",
                            "amount": 26.98,
                            "unit": "g",
                            "percentOfDailyNeeds": 52.91
                        },
                        {
                            "name": "Saturated Fat",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 138.71
                        },
                        {
                            "name": "Vitamin B12",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 1.2
                        },
                        {
                            "name": "Fiber",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 32.33
                        },
                        {
                            "name": "Vitamin A",
                            "amount": 0.0,
                            "unit": "IU",
                            "percentOfDailyNeeds": 23.17
                        },
                        {
                            "name": "Vitamin B2",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.95
                        },
                        {
                            "name": "Vitamin B3",
                            "amount": 0.03,
                            "unit": "mg",
                            "percentOfDailyNeeds": 5.22
                        },
                        {
                            "name": "Poly Unsaturated Fat",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Phosphorus",
                            "amount": 1.1,
                            "unit": "mg",
                            "percentOfDailyNeeds": 16.47
                        },
                        {
                            "name": "Vitamin E",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.35
                        },
                        {
                            "name": "Zinc",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.77
                        },
                        {
                            "name": "Mono Unsaturated Fat",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Alcohol",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B1",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.37
                        },
                        {
                            "name": "Cholesterol",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 30.42
                        },
                        {
                            "name": "Selenium",
                            "amount": 0.33,
                            "unit": "µg",
                            "percentOfDailyNeeds": 18.39
                        },
                        {
                            "name": "Folic Acid",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Lycopene",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Folate",
                            "amount": 0.28,
                            "unit": "µg",
                            "percentOfDailyNeeds": 7.53
                        },
                        {
                            "name": "Choline",
                            "amount": 0.63,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B5",
                            "amount": 0.04,
                            "unit": "mg",
                            "percentOfDailyNeeds": 7.18
                        },
                        {
                            "name": "Vitamin D",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 4.24
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 26.98,
                            "unit": "g",
                            "percentOfDailyNeeds": 51.19
                        },
                        {
                            "name": "Vitamin B6",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 6.87
                        },
                        {
                            "name": "Sugar",
                            "amount": 26.67,
                            "unit": "g",
                            "percentOfDailyNeeds": 131.93
                        },
                        {
                            "name": "Caffeine",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Manganese",
                            "amount": 0.02,
                            "unit": "mg",
                            "percentOfDailyNeeds": 70.98
                        },
                        {
                            "name": "Magnesium",
                            "amount": 2.47,
                            "unit": "mg",
                            "percentOfDailyNeeds": 14.68
                        },
                        {
                            "name": "Sodium",
                            "amount": 7.7,
                            "unit": "mg",
                            "percentOfDailyNeeds": 1.08
                        },
                        {
                            "name": "Fat",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 56.81
                        },
                        {
                            "name": "Vitamin C",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.45
                        },
                        {
                            "name": "Vitamin K",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 8.43
                        },
                        {
                            "name": "Calcium",
                            "amount": 22.83,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.48
                        }
                    ]
                },
                {
                    "id": 20081,
                    "name": "flour",
                    "amount": 0.06,
                    "unit": "cup",
                    "nutrients": [
                        {
                            "name": "Protein",
                            "amount": 0.81,
                            "unit": "g",
                            "percentOfDailyNeeds": 11.6
                        },
                        {
                            "name": "Copper",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 11.4
                        },
                        {
                            "name": "Iron",
                            "amount": 0.36,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.02
                        },
                        {
                            "name": "Potassium",
                            "amount": 8.36,
                            "unit": "mg",
                            "percentOfDailyNeeds": 10.76
                        },
                        {
                            "name": "Calories",
                            "amount": 28.44,
                            "unit": "kcal",
                            "percentOfDailyNeeds": 46.88
                        },
                        {
                            "name": "Net Carbohydrates",
                            "amount": 5.75,
                            "unit": "g",
                            "percentOfDailyNeeds": 52.91
                        },
                        {
                            "name": "Saturated Fat",
                            "amount": 0.01,
                            "unit": "g",
                            "percentOfDailyNeeds": 138.71
                        },
                        {
                            "name": "Vitamin B12",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 1.2
                        },
                        {
                            "name": "Fiber",
                            "amount": 0.21,
                            "unit": "g",
                            "percentOfDailyNeeds": 32.33
                        },
                        {
                            "name": "Vitamin A",
                            "amount": 0.0,
                            "unit": "IU",
                            "percentOfDailyNeeds": 23.17
                        },
                        {
                            "name": "Vitamin B2",
                            "amount": 0.04,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.95
                        },
                        {
                            "name": "Vitamin B3",
                            "amount": 0.46,
                            "unit": "mg",
                            "percentOfDailyNeeds": 5.22
                        },
                        {
                            "name": "Poly Unsaturated Fat",
                            "amount": 0.03,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Phosphorus",
                            "amount": 8.44,
                            "unit": "mg",
                            "percentOfDailyNeeds": 16.47
                        },
                        {
                            "name": "Vitamin E",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.35
                        },
                        {
                            "name": "Zinc",
                            "amount": 0.05,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.77
                        },
                        {
                            "name": "Mono Unsaturated Fat",
                            "amount": 0.01,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Alcohol",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B1",
                            "amount": 0.06,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.37
                        },
                        {
                            "name": "Cholesterol",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 30.42
                        },
                        {
                            "name": "Selenium",
                            "amount": 2.65,
                            "unit": "µg",
                            "percentOfDailyNeeds": 18.39
                        },
                        {
                            "name": "Folic Acid",
                            "amount": 12.03,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Lycopene",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Folate",
                            "amount": 14.3,
                            "unit": "µg",
                            "percentOfDailyNeeds": 7.53
                        },
                        {
                            "name": "Choline",
                            "amount": 0.81,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B5",
                            "amount": 0.03,
                            "unit": "mg",
                            "percentOfDailyNeeds": 7.18
                        },
                        {
                            "name": "Vitamin D",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 4.24
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 5.96,
                            "unit": "g",
                            "percentOfDailyNeeds": 51.19
                        },
                        {
                            "name": "Vitamin B6",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 6.87
                        },
                        {
                            "name": "Sugar",
                            "amount": 0.02,
                            "unit": "g",
                            "percentOfDailyNeeds": 131.93
                        },
                        {
                            "name": "Caffeine",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Manganese",
                            "amount": 0.05,
                            "unit": "mg",
                            "percentOfDailyNeeds": 70.98
                        },
                        {
                            "name": "Magnesium",
                            "amount": 1.72,
                            "unit": "mg",
                            "percentOfDailyNeeds": 14.68
                        },
                        {
                            "name": "Sodium",
                            "amount": 0.16,
                            "unit": "mg",
                            "percentOfDailyNeeds": 1.08
                        },
                        {
                            "name": "Fat",
                            "amount": 0.08,
                            "unit": "g",
                            "percentOfDailyNeeds": 56.81
                        },
                        {
                            "name": "Vitamin C",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.45
                        },
                        {
                            "name": "Vitamin K",
                            "amount": 0.02,
                            "unit": "µg",
                            "percentOfDailyNeeds": 8.43
                        },
                        {
                            "name": "Calcium",
                            "amount": 1.17,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.48
                        }
                    ]
                },
                {
                    "id": 1145,
                    "name": "butter",
                    "amount": 0.25,
                    "unit": "stick",
                    "nutrients": [
                        {
                            "name": "Protein",
                            "amount": 0.24,
                            "unit": "g",
                            "percentOfDailyNeeds": 11.6
                        },
                        {
                            "name": "Copper",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 11.4
                        },
                        {
                            "name": "Iron",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.02
                        },
                        {
                            "name": "Potassium",
                            "amount": 6.78,
                            "unit": "mg",
                            "percentOfDailyNeeds": 10.76
                        },
                        {
                            "name": "Calories",
                            "amount": 202.55,
                            "unit": "kcal",
                            "percentOfDailyNeeds": 46.88
                        },
                        {
                            "name": "Net Carbohydrates",
                            "amount": 0.02,
                            "unit": "g",
                            "percentOfDailyNeeds": 52.91
                        },
                        {
                            "name": "Saturated Fat",
                            "amount": 14.51,
                            "unit": "g",
                            "percentOfDailyNeeds": 138.71
                        },
                        {
                            "name": "Vitamin B12",
                            "amount": 0.05,
                            "unit": "µg",
                            "percentOfDailyNeeds": 1.2
                        },
                        {
                            "name": "Vitamin B2",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.95
                        },
                        {
                            "name": "Vitamin A",
                            "amount": 705.97,
                            "unit": "IU",
                            "percentOfDailyNeeds": 23.17
                        },
                        {
                            "name": "Fiber",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 32.33
                        },
                        {
                            "name": "Vitamin B3",
                            "amount": 0.01,
                            "unit": "mg",
                            "percentOfDailyNeeds": 5.22
                        },
                        {
                            "name": "Poly Unsaturated Fat",
                            "amount": 0.86,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Phosphorus",
                            "amount": 6.78,
                            "unit": "mg",
                            "percentOfDailyNeeds": 16.47
                        },
                        {
                            "name": "Fluoride",
                            "amount": 0.79,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin E",
                            "amount": 0.66,
                            "unit": "mg",
                            "percentOfDailyNeeds": 13.35
                        },
                        {
                            "name": "Zinc",
                            "amount": 0.03,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.77
                        },
                        {
                            "name": "Mono Unsaturated Fat",
                            "amount": 5.94,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Trans Fat",
                            "amount": 0.93,
                            "unit": "g",
                            "percentOfDailyNeeds": 13915.11
                        },
                        {
                            "name": "Alcohol",
                            "amount": 0.0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B1",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.37
                        },
                        {
                            "name": "Cholesterol",
                            "amount": 60.74,
                            "unit": "mg",
                            "percentOfDailyNeeds": 30.42
                        },
                        {
                            "name": "Selenium",
                            "amount": 0.28,
                            "unit": "µg",
                            "percentOfDailyNeeds": 18.39
                        },
                        {
                            "name": "Folic Acid",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Lycopene",
                            "amount": 0.0,
                            "unit": "µg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Folate",
                            "amount": 0.85,
                            "unit": "µg",
                            "percentOfDailyNeeds": 7.53
                        },
                        {
                            "name": "Choline",
                            "amount": 5.31,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Vitamin B5",
                            "amount": 0.03,
                            "unit": "mg",
                            "percentOfDailyNeeds": 7.18
                        },
                        {
                            "name": "Vitamin D",
                            "amount": 0.42,
                            "unit": "µg",
                            "percentOfDailyNeeds": 4.24
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 0.02,
                            "unit": "g",
                            "percentOfDailyNeeds": 51.19
                        },
                        {
                            "name": "Vitamin B6",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 6.87
                        },
                        {
                            "name": "Sugar",
                            "amount": 0.02,
                            "unit": "g",
                            "percentOfDailyNeeds": 131.93
                        },
                        {
                            "name": "Caffeine",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 0.0
                        },
                        {
                            "name": "Manganese",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 70.98
                        },
                        {
                            "name": "Magnesium",
                            "amount": 0.56,
                            "unit": "mg",
                            "percentOfDailyNeeds": 14.68
                        },
                        {
                            "name": "Sodium",
                            "amount": 3.11,
                            "unit": "mg",
                            "percentOfDailyNeeds": 1.08
                        },
                        {
                            "name": "Fat",
                            "amount": 22.91,
                            "unit": "g",
                            "percentOfDailyNeeds": 56.81
                        },
                        {
                            "name": "Vitamin C",
                            "amount": 0.0,
                            "unit": "mg",
                            "percentOfDailyNeeds": 15.45
                        },
                        {
                            "name": "Vitamin K",
                            "amount": 1.98,
                            "unit": "µg",
                            "percentOfDailyNeeds": 8.43
                        },
                        {
                            "name": "Calcium",
                            "amount": 6.78,
                            "unit": "mg",
                            "percentOfDailyNeeds": 8.48
                        }
                    ]
                }
            ],
            "caloricBreakdown": {
                "percentProtein": 2.39,
                "percentFat": 34.27,
                "percentCarbs": 63.34
            },
            "weightPerServing": {
                "amount": 361,
                "unit": "g"
            }
        },
        "taste": {
            "sweetness": 100.0,
            "saltiness": 0.3,
            "sourness": 17.63,
            "bitterness": 5.19,
            "savoriness": 1.46,
            "fattiness": 26.03,
            "spiciness": 0.0
        },
        "summary": "Need a <b>lacto ovo vegetarian dessert</b>? Cranberry Apple Crisp could be an excellent recipe to try. This recipe serves 4. One serving contains <b>833 calories</b>, <b>6g of protein</b>, and <b>37g of fat</b>. For <b>$1.54 per serving</b>, this recipe <b>covers 13%</b> of your daily requirements of vitamins and minerals. 11 person were glad they tried this recipe. From preparation to the plate, this recipe takes roughly <b>45 minutes</b>. If you have butter, regular oats, sugar, and a few other ingredients on hand, you can make it. It is brought to you by Foodista. Overall, this recipe earns a <b>not so awesome spoonacular score of 36%</b>. If you like this recipe, you might also like recipes such as <a href=\"https://spoonacular.com/recipes/apple-cranberry-crisp-55221\">Apple Cranberry Crisp</a>, <a href=\"https://spoonacular.com/recipes/the-best-cranberry-apple-crisp-1053025\">The Best Cranberry Apple Crisp</a>, and <a href=\"https://spoonacular.com/recipes/apple-cranberry-crisp-128913\">Apple Cranberry Crisp</a>.",
        "cuisines": [],
        "dishTypes": [
            "dessert"
        ],
        "diets": [
            "lacto ovo vegetarian"
        ],
        "occasions": [],
        "winePairing": {
            "pairedWines": [
                "cream sherry",
                "port wine",
                "moscato dasti"
            ],
            "pairingText": "Cream Sherry, Port Wine, and Moscato d'Asti are my top picks for Crisp. A common wine pairing rule is to make sure your wine is sweeter than your food. Delicate desserts go well with Moscato d'Asti, nutty desserts with cream sherry, and caramel or chocolate desserts pair well with port. The NV Johnson Estate Cream Sherry with a 5 out of 5 star rating seems like a good match. It costs about 19 dollars per bottle.",
            "productMatches": [
                {
                    "id": 430626,
                    "title": "NV Johnson Estate Cream Sherry",
                    "description": "Very aromatic with notes of hazelnut, vanilla, and a touch of oak followed by sweet raisins and a touch of yeast. Clean lasting finish. Good now but will reward those allow it to age\"\". A favorite pre-prandial beverage. Consider it with nuts before dinner as an aperitif, or after dinner with dessert, especially chocolates and fruit-based desserts. Also wonderful on cold afternoons, served with biscotti to dip in \"\"Italian-style\"\". \"",
                    "price": "$19.49",
                    "imageUrl": "https://img.spoonacular.com/products/430626-312x231.jpg",
                    "averageRating": 1.0,
                    "ratingCount": 2.0,
                    "score": 0.8571,
                    "link": "https://www.amazon.com/Johnson-Estate-Cream-Sherry-750/dp/B00D3GQSRW?tag=spoonacular-20"
                }
            ]
        },
        "instructions": "Preheat the oven to 350 degrees and grease or butter a 913 glass baking dish.\nIn a large bowl, toss together the chopped apples, cranberries and sugar. Let stand for a few minutes then pour into the baking dish.\nDot the mixture with the 1/2 stick of cubed butter.\nIn a medium bowl, combine the oats, brown sugar and flour.  Sprinkle evenly over the cranberries and apples in the baking dish.  Gently pour the melted butter over the top.\nCover with aluminum foil and bake for 35 minutes.  Remove the foil and bake for an additional 15 minutes, or until the oat topping is nicely browned.\nServe warm as a side or for dessert with a scoop of vanilla ice cream.",
        "analyzedInstructions": [
            {
                "name": "",
                "steps": [
                    {
                        "number": 1,
                        "step": "Preheat the oven to 350 degrees and grease or butter a 913 glass baking dish.",
                        "ingredients": [
                            {
                                "id": 1001,
                                "name": "butter",
                                "localizedName": "butter",
                                "image": "https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg"
                            }
                        ],
                        "equipment": [
                            {
                                "id": 406921,
                                "name": "glass baking pan",
                                "localizedName": "glass baking pan",
                                "image": "https://spoonacular.com/cdn/equipment_100x100/glass-baking-tray.jpg"
                            },
                            {
                                "id": 404784,
                                "name": "oven",
                                "localizedName": "oven",
                                "image": "https://spoonacular.com/cdn/equipment_100x100/oven.jpg"
                            }
                        ]
                    },
                    {
                        "number": 2,
                        "step": "In a large bowl, toss together the chopped apples, cranberries and sugar.",
                        "ingredients": [
                            {
                                "id": 9078,
                                "name": "cranberries",
                                "localizedName": "cranberries",
                                "image": "https://spoonacular.com/cdn/ingredients_100x100/cranberries.jpg"
                            },
                            {
                                "id": 9003,
                                "name": "apple",
                                "localizedName": "apple",
                                "image": "https://spoonacular.com/cdn/ingredients_100x100/apple.jpg"
                            },
                            {
                                "id": 19335,
                                "name": "sugar",
                                "localizedName": "sugar",
                                "image": "https://spoonacular.com/cdn/ingredients_100x100/sugar-in-bowl.png"
                            }
                        ],
                        "equipment": [
                            {
                                "id": 404783,
                                "name": "bowl",
                                "localizedName": "bowl",
                                "image": "https://spoonacular.com/cdn/equipment_100x100/bowl.jpg"
                            }
                        ]
                    },
                    {
                        "number": 3,
                        "step": "Let stand for a few minutes then pour into the baking dish.",
                        "ingredients": [],
                        "equipment": [
                            {
                                "id": 404646,
                                "name": "baking pan",
                                "localizedName": "baking pan",
                                "image": "https://spoonacular.com/cdn/equipment_100x100/roasting-pan.jpg"
                            }
                        ]
                    },
                    {
                        "number": 4,
                        "step": "Dot the mixture with the 1/2 stick of cubed butter.",
                        "ingredients": [
                            {
                                "id": 1001,
                                "name": "butter",
                                "localizedName": "butter",
                                "image": "https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg"
                            }
                        ],
                        "equipment": []
                    },
                    {
                        "number": 5,
                        "step": "In a medium bowl, combine the oats, brown sugar and flour.",
                        "ingredients": [
                            {
                                "id": 19334,
                                "name": "brown sugar",
                                "localizedName": "brown sugar",
                                "image": "https://spoonacular.com/cdn/ingredients_100x100/dark-brown-sugar.png"
                            },
                            {
                                "id": 20081,
                                "name": "all purpose flour",
                                "localizedName": "all purpose flour",
                                "image": "https://spoonacular.com/cdn/ingredients_100x100/flour.png"
                            },
                            {
                                "id": 8120,
                                "name": "oats",
                                "localizedName": "oats",
                                "image": "https://spoonacular.com/cdn/ingredients_100x100/rolled-oats.jpg"
                            }
                        ],
                        "equipment": [
                            {
                                "id": 404783,
                                "name": "bowl",
                                "localizedName": "bowl",
                                "image": "https://spoonacular.com/cdn/equipment_100x100/bowl.jpg"
                            }
                        ]
                    },
                    {
                        "number": 6,
                        "step": "Sprinkle evenly over the cranberries and apples in the baking dish.  Gently pour the melted butter over the top.",
                        "ingredients": [
                            {
                                "id": 9078,
                                "name": "cranberries",
                                "localizedName": "cranberries",
                                "image": "https://spoonacular.com/cdn/ingredients_100x100/cranberries.jpg"
                            },
                            {
                                "id": 9003,
                                "name": "apple",
                                "localizedName": "apple",
                                "image": "https://spoonacular.com/cdn/ingredients_100x100/apple.jpg"
                            },
                            {
                                "id": 1001,
                                "name": "butter",
                                "localizedName": "butter",
                                "image": "https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg"
                            }
                        ],
                        "equipment": [
                            {
                                "id": 404646,
                                "name": "baking pan",
                                "localizedName": "baking pan",
                                "image": "https://spoonacular.com/cdn/equipment_100x100/roasting-pan.jpg"
                            }
                        ]
                    },
                    {
                        "number": 7,
                        "step": "Cover with aluminum foil and bake for 35 minutes.",
                        "ingredients": [],
                        "equipment": [
                            {
                                "id": 404765,
                                "name": "aluminum foil",
                                "localizedName": "aluminum foil",
                                "image": "https://spoonacular.com/cdn/equipment_100x100/aluminum-foil.png"
                            },
                            {
                                "id": 404784,
                                "name": "oven",
                                "localizedName": "oven",
                                "image": "https://spoonacular.com/cdn/equipment_100x100/oven.jpg"
                            }
                        ],
                        "length": {
                            "number": 35,
                            "unit": "minutes"
                        }
                    },
                    {
                        "number": 8,
                        "step": "Remove the foil and bake for an additional 15 minutes, or until the oat topping is nicely browned.",
                        "ingredients": [],
                        "equipment": [
                            {
                                "id": 404784,
                                "name": "oven",
                                "localizedName": "oven",
                                "image": "https://spoonacular.com/cdn/equipment_100x100/oven.jpg"
                            },
                            {
                                "id": 404765,
                                "name": "aluminum foil",
                                "localizedName": "aluminum foil",
                                "image": "https://spoonacular.com/cdn/equipment_100x100/aluminum-foil.png"
                            }
                        ],
                        "length": {
                            "number": 15,
                            "unit": "minutes"
                        }
                    },
                    {
                        "number": 9,
                        "step": "Serve warm as a side or for dessert with a scoop of vanilla ice cream.",
                        "ingredients": [
                            {
                                "id": 19095,
                                "name": "vanilla ice cream",
                                "localizedName": "vanilla ice cream",
                                "image": "https://spoonacular.com/cdn/ingredients_100x100/vanilla-ice-cream.png"
                            }
                        ],
                        "equipment": []
                    }
                ]
            }
        ],
        "originalId": None,
        "spoonacularScore": 0.34228065609931946,
        "spoonacularSourceUrl": "https://spoonacular.com/cranberry-apple-crisp-640352"
    }

    nutrients = response.get("nutrition").get("nutrients")
    carbohydrates = next((nutrient for nutrient in nutrients if nutrient.get(
        'name') == 'Carbohydrates'), None)
    protein = next((nutrient for nutrient in nutrients if nutrient.get(
        'name') == 'Protein'), None)
    calories = next((nutrient for nutrient in nutrients if nutrient.get(
        'name') == 'Calories'), None)

    return {
        "carbohydrates": carbohydrates.get("amount"),
        "protein": protein.get("amount"),
        "calories": calories.get("amount")
    }


@app.get("/recipes")
async def get_recipes(ingredients: str, numberofRecipes: int):
    external_api_url = "https://api.spoonacular.com/recipes/findByIngredients"
    try:
        response = requests.get(
            external_api_url,
            params={
                "ingredients": ingredients,
                "number": numberofRecipes,
                "apiKey": "fe63e207cd4545b2a58adbf684fdb251"
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/recipe/{recipe_id}")
async def get_nutrition(recipe_id: int):
    external_api_url = f"https://api.spoonacular.com/recipes/"
    f"{recipe_id}/information"
    try:
        response = requests.get(
            external_api_url,
            params={
                "includeNutrition": "True",
                "apiKey": "fe63e207cd4545b2a58adbf684fdb251"
            }
        )

        response.raise_for_status()

        nutrients = response.json().get("nutrition").get("nutrients")
        carbohydrates = next((nutrient for nutrient in nutrients if nutrient.get(
            'name') == 'Carbohydrates'), None)
        protein = next((nutrient for nutrient in nutrients if nutrient.get(
            'name') == 'Protein'), None)
        calories = next((nutrient for nutrient in nutrients if nutrient.get(
            'name') == 'Calories'), None)

        return {
            "carbohydrates": carbohydrates.get("amount"),
            "protein": protein.get("amount"),
            "calories": calories.get("amount")
        }

    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))
