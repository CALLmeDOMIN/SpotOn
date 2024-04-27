import { type Nutrition, type Recipe } from "@/lib/types";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "./ui/card";
import { useQuery } from "@tanstack/react-query";
import Loader from "./Loader";

const fetchNutrition = async (id: number) => {
  const res = await fetch(`/api/${id}`);
  return res.json();
};

const RecipeTile = ({ recipe }: { recipe: Recipe }) => {
  const { data, isLoading, isError, error } = useQuery<Nutrition>({
    queryKey: ["nutrition", recipe.id],
    queryFn: () => fetchNutrition(recipe.id),
  });

  if (isLoading) return <Loader />;
  if (isError) return <p>Error: {error.message}</p>;

  return (
    <Card className="flex transition-all hover:scale-105">
      <div className="m-4 hidden items-center justify-center md:flex">
        <img
          src={recipe.image}
          alt={recipe.title}
          className="h-32 w-32 rounded-lg object-cover"
        />
      </div>
      <div className="flex grow flex-col">
        <CardHeader className="md:pl-0">
          <CardTitle>{recipe.title}</CardTitle>
          <CardDescription className="text-green-500">
            {recipe.usedIngredients.map((i) => i.name).join(", ")}
          </CardDescription>
          <CardDescription className="text-red-500">
            {recipe.missedIngredients.map((i) => i.name).join(", ")}
          </CardDescription>
        </CardHeader>
        <CardContent className="px-0 md:hidden">
          <div className="flex items-center justify-center">
            <img
              src={recipe.image}
              alt={recipe.title}
              className="w-full object-cover"
            />
          </div>
        </CardContent>
        <CardContent className="flex justify-center space-x-2 md:justify-end md:pl-0">
          <div className="flex min-w-20 flex-col items-center justify-center rounded-md border p-2 shadow-md">
            <p className="font-bold">{data?.carbohydrates}</p>
            <p className="text-sm font-semibold">Carbs</p>
            <p className="text-sm text-slate-300">g</p>
          </div>
          <div className="flex min-w-20 flex-col items-center justify-center rounded-md border p-2 shadow-md">
            <p className="font-bold">{data?.protein}</p>
            <p className="text-sm font-semibold">Protein</p>
            <p className="text-sm text-slate-300">g</p>
          </div>
          <div className="flex min-w-20 flex-col items-center justify-center rounded-md border p-2 shadow-md">
            <p className="font-bold">{data?.calories}</p>
            <p className="text-sm font-semibold">Calories</p>
            <p className="text-sm text-slate-300">Kcal</p>
          </div>
        </CardContent>
      </div>
    </Card>
  );
};

export default RecipeTile;
