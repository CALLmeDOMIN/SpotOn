from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():  # mock
    res = {
        "results": [
            {
                "id": 654959,
                "title": "Pasta With Tuna",
                "image": "https://img.spoonacular.com/recipes/654959-312x231.jpg",
                "imageType": "jpg",
                "nutrition": {
                    "nutrients": [
                        {
                            "name": "Fat",
                            "amount": 10.3185,
                            "unit": "g"
                        }
                    ]
                }
            }
        ],
        "offset": 0,
        "number": 1,
        "totalResults": 133
    }

    return res.get("results")
