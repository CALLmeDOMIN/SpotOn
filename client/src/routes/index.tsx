import { createFileRoute } from "@tanstack/react-router";
import RecipiesForm from "@/components/RecipesForm";

export const Route = createFileRoute("/")({
  component: () => <Home />,
});

const Home = () => {
  return (
    <>
      <div className="flex min-h-screen items-center justify-center">
        <RecipiesForm />
      </div>
    </>
  );
};
