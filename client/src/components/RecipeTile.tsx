import { type Recipe } from "@/lib/types";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "./ui/card";

const RecipeTile = ({ recipe }: { recipe: Recipe }) => {
  return (
    <Card className="flex">
      <div className="m-4 flex items-center justify-center">
        <img
          src={recipe.image}
          alt={recipe.title}
          className="h-32 w-32 rounded-lg object-cover"
        />
      </div>
      <div className="flex flex-col">
        <CardHeader className="pl-0">
          <CardTitle>{recipe.title}</CardTitle>
          <CardDescription>{recipe.id}</CardDescription>
        </CardHeader>
        <CardContent className="pl-0">
          <p>Card Content</p>
        </CardContent>
        <CardFooter className="pl-0">
          <p>Card Footer</p>
        </CardFooter>
      </div>
    </Card>
  );
};

export default RecipeTile;
