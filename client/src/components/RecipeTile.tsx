import { type Recipe } from "@/lib/types";

const RecipeTile = ({ recipe }: { recipe: Recipe }) => {
  return <div>{recipe.title}</div>;
};

export default RecipeTile;
