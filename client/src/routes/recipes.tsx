import { type Recipe, type RecipesSearch } from "@/lib/types";
import { createFileRoute } from "@tanstack/react-router";
import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import RecipesForm from "@/components/RecipesForm";
import RecipeTile from "@/components/RecipeTile";

export const Route = createFileRoute("/recipes")({
  component: () => <Recipes />,
});

const fetchData = async () => {
  const res = await axios.get("/api");
  return res.data;
};

const Recipes = () => {
  const { ingridients, numberOfRecipes }: RecipesSearch = Route.useSearch();

  const { data, isLoading, isError, error } = useQuery({
    queryKey: ["data"],
    queryFn: fetchData,
  });

  if (isLoading) {
    return <h1>Loading...</h1>;
  }

  if (isError) {
    return <h1>Error: {JSON.stringify(error.message)}</h1>;
  }

  return (
    <div className="grid min-h-screen grid-cols-5">
      <div className="col-span-2 flex h-full items-center justify-center">
        <RecipesForm
          className="m-8 flex items-center"
          defaultValues={{ ingridients, numberOfRecipes }}
        />
      </div>
      <div className="col-span-3 mt-10 max-h-[calc(100vh_-_2.5rem)] overflow-auto">
        <div className="flex w-3/4 flex-col space-y-4">
          {data &&
            data.map((recipe: Recipe) => (
              <RecipeTile key={recipe.id} recipe={recipe} />
            ))}
        </div>
      </div>
    </div>
  );
};
