import { type Recipe, type RecipesSearch } from "@/lib/types";
import { createFileRoute } from "@tanstack/react-router";
import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import RecipesForm from "@/components/RecipesForm";
import RecipeTile from "@/components/RecipeTile";
import { ArrowUp } from "lucide-react";
import { useEffect, useState } from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
} from "@/components/ui/card";
import { toast } from "sonner";

export const Route = createFileRoute("/recipes")({
  component: () => <Recipes />,
});

const fetchRecipes = async (ingredients: string, numberOfRecipes: number) => {
  const res = await axios.get("/api/recipes", {
    params: { ingredients, numberOfRecipes },
  });
  return res.data;
};

const Recipes = () => {
  const { ingredients, numberOfRecipes }: RecipesSearch = Route.useSearch();

  const { data, isLoading, isError } = useQuery({
    queryKey: ["data"],
    queryFn: () => fetchRecipes(ingredients, numberOfRecipes),
    retry: 1,
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
            [...Array(numberOfRecipes)].map((_, i) => (
              <RecipesFormLoading key={i} />
            ))
          ) : isError ? (
            <>
              {toast.error("Error fetching recipes")}
              <h1>No recipes found</h1>
              <p>
                Might be caused by using all of the API points. If that's the
                case - come back tommorow
              </p>
            </>
          ) : data?.length !== 0 ? (
            data.map((recipe: Recipe) => (
              <RecipeTile key={recipe.id} recipe={recipe} />
            ))
          ) : (
            <h1>No recipes found</h1>
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

const RecipesFormLoading = () => {
  return (
    <Card className="flex transition-all hover:scale-105">
      <div className="m-4 hidden items-center justify-center md:flex">
        <div className="flex h-32 w-32 animate-pulse items-center justify-center rounded-lg bg-gray-300 dark:bg-gray-700">
          <svg
            className="h-10 w-10 text-gray-200 dark:text-gray-600"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 20 18"
          >
            <path d="M18 0H2a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm4.376 10.481A1 1 0 0 1 16 15H4a1 1 0 0 1-.895-1.447l3.5-7A1 1 0 0 1 7.468 6a.965.965 0 0 1 .9.5l2.775 4.757 1.546-1.887a1 1 0 0 1 1.618.1l2.541 4a1 1 0 0 1 .028 1.011Z" />
          </svg>
        </div>
      </div>
      <div className="flex grow flex-col">
        <CardHeader className="md:pl-0">
          <div className="mb-4 h-4 w-48 animate-pulse rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <CardDescription className="text-green-500">
            <div className="mb-2.5 h-2 animate-pulse rounded-full bg-gray-200 dark:bg-gray-700"></div>
          </CardDescription>
          <CardDescription className="text-red-500">
            <div className="mb-2.5 h-2 max-w-[440px] animate-pulse rounded-full bg-gray-200 dark:bg-gray-700"></div>
          </CardDescription>
        </CardHeader>
        <CardContent className="px-0 md:hidden">
          <div className="flex items-center justify-center">
            <div className="flex h-32 w-32 animate-pulse items-center justify-center rounded-lg bg-gray-300 dark:bg-gray-700">
              <svg
                className="h-10 w-10 text-gray-200 dark:text-gray-600"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="currentColor"
                viewBox="0 0 20 18"
              >
                <path d="M18 0H2a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm4.376 10.481A1 1 0 0 1 16 15H4a1 1 0 0 1-.895-1.447l3.5-7A1 1 0 0 1 7.468 6a.965.965 0 0 1 .9.5l2.775 4.757 1.546-1.887a1 1 0 0 1 1.618.1l2.541 4a1 1 0 0 1 .028 1.011Z" />
              </svg>
            </div>
          </div>
        </CardContent>
        <CardContent className="flex justify-center space-x-2 md:justify-end md:pl-0">
          <div className="flex min-w-20 flex-col items-center justify-center rounded-md border p-2 shadow-md">
            <div className="flex h-4 w-8 animate-pulse items-center justify-center rounded-lg bg-gray-300 dark:bg-gray-700"></div>
            <p className="text-sm font-semibold">Carbs</p>
            <p className="text-sm text-slate-300">g</p>
          </div>
          <div className="flex min-w-20 flex-col items-center justify-center rounded-md border p-2 shadow-md">
            <div className="flex h-4 w-8 animate-pulse items-center justify-center rounded-lg bg-gray-300 dark:bg-gray-700"></div>
            <p className="text-sm font-semibold">Protein</p>
            <p className="text-sm text-slate-300">g</p>
          </div>
          <div className="flex min-w-20 flex-col items-center justify-center rounded-md border p-2 shadow-md">
            <div className="flex h-4 w-8 animate-pulse items-center justify-center rounded-lg bg-gray-300 dark:bg-gray-700"></div>
            <p className="text-sm font-semibold">Calories</p>
            <p className="text-sm text-slate-300">Kcal</p>
          </div>
        </CardContent>
      </div>
    </Card>
  );
};
