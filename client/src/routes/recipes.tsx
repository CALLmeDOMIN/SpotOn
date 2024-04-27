import { type Recipe, type RecipesSearch } from "@/lib/types";
import { createFileRoute } from "@tanstack/react-router";
import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import RecipesForm from "@/components/RecipesForm";
import RecipeTile from "@/components/RecipeTile";
import { ArrowUp } from "lucide-react";
import { useEffect, useState } from "react";
import Loader from "@/components/Loader";

export const Route = createFileRoute("/recipes")({
  component: () => <Recipes />,
});

// const fetchData = async (ingredients: string, numberOfRecipes: number) => {
//   const res = await axios.get("/api", {
//     params: { ingredients, numberOfRecipes },
//   });
//   return res;
// };

const fetchData = async () => {
  const res = await axios.get("/api");
  return res.data;
};

const Recipes = () => {
  const { ingredients, numberOfRecipes }: RecipesSearch = Route.useSearch();

  const { data, isLoading, isError, error } = useQuery({
    queryKey: ["data"],
    // queryFn: () => fetchData(ingredients, numberOfRecipes)
    queryFn: fetchData,
  });

  const [showScrollButton, setShowScrollButton] = useState(false);

  useEffect(() => {
    const checkScroll = () => {
      setShowScrollButton(window.scrollY > 200);
    };

    window.addEventListener("scroll", checkScroll);
    return () => window.removeEventListener("scroll", checkScroll);
  }, []);

  return (
    <div className="min-h-screen md:grid md:grid-cols-5">
      <div className="col-span-2 m-8 flex items-center justify-center ">
        <RecipesForm defaultValues={{ ingredients, numberOfRecipes }} />
      </div>
      <div className="mt-10 md:col-span-3 md:max-h-[calc(100vh_-_2.5rem)] md:overflow-auto">
        <div className="flex flex-col space-y-4 p-6 md:p-10 lg:w-3/4">
          {isLoading ? (
            <Loader />
          ) : isError ? (
            <h1>Error: {JSON.stringify(error.message)}</h1>
          ) : (
            data.map((recipe: Recipe) => (
              <RecipeTile key={recipe.id} recipe={recipe} />
            ))
          )}
        </div>
      </div>
      {showScrollButton && (
        <button
          onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
          className="fixed bottom-5 right-5 flex h-10 w-10 items-center justify-center rounded-full border bg-background md:hidden"
        >
          <ArrowUp />
        </button>
      )}
    </div>
  );
};
