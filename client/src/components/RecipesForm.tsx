import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { RecipesSearch } from "@/lib/types";
import { useNavigate } from "@tanstack/react-router";

const formSchema = z.object({
  ingredients: z.string().min(1, { message: "Ingredients are required" }),
  numberOfRecipes: z.number().positive().max(10, {
    message: "Max number of recipes is 10",
  }),
});

const RecipesForm = ({
  className,
  defaultValues,
}: {
  className?: string;
  defaultValues?: RecipesSearch;
}) => {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      ingredients: defaultValues?.ingredients || "",
      numberOfRecipes: defaultValues?.numberOfRecipes || 1,
    },
  });

  const navigate = useNavigate();

  const onSubmit = (values: z.infer<typeof formSchema>) => {
    navigate({
      to: "/recipes",
      search: {
        ingredients: values.ingredients,
        numberOfRecipes: values.numberOfRecipes,
      },
    });
  };

  return (
    <div className={className}>
      <Form {...form}>
        <form className="space-y-8" onSubmit={form.handleSubmit(onSubmit)}>
          <FormField
            control={form.control}
            name="ingredients"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Ingredients</FormLabel>
                <FormControl>
                  <Input placeholder="Your typical Ingredients" {...field} />
                </FormControl>
                <FormDescription>
                  Input what you got in your fridge.
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="numberOfRecipes"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Number of Recipes</FormLabel>
                <FormControl>
                  <Input
                    type="number"
                    {...field}
                    {...form.register("numberOfRecipes", {
                      valueAsNumber: true,
                    })}
                  />
                </FormControl>
                <FormDescription>
                  Amount of recipes you want to see.
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />
          <div className="flex justify-center">
            <Button type="submit">Submit</Button>
          </div>
        </form>
      </Form>
    </div>
  );
};

export default RecipesForm;
