export type RecipesSearch = {
  ingredients: string;
  numberOfRecipes: number;
};

export type Recipe = {
  id: number;
  image: string;
  title: string;
  missedIngredients: Ingridient[];
  usedIngredients: Ingridient[];
};

type Ingridient = {
  name: string;
};

export type Nutrition = {
  carbohydrates: number;
  protein: number;
  calories: number;
};
