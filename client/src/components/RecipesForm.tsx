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
import { Link } from "@tanstack/react-router";
import { RecipesSearch } from "@/lib/types";

const formSchema = z.object({
  ingridients: z.string().min(1),
  numberOfRecipes: z.number().int().positive(),
});

const RecipesForm = ({
  className,
  defaultValues,
}: {
  className: string;
  defaultValues?: RecipesSearch;
}) => {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      ingridients: "",
      numberOfRecipes: 1,
    },
  });

  return (
    <div className={className}>
      <Form {...form}>
        <form className="space-y-8">
          <FormField
            control={form.control}
            name="ingridients"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Ingridients</FormLabel>
                <FormControl>
                  <Input
                    placeholder="Your typical Ingridients"
                    {...field}
                    defaultValue={defaultValues?.ingridients}
                  />
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
                    defaultValue={defaultValues?.numberOfRecipes}
                  />
                </FormControl>
                <FormDescription>
                  How many recipes do you want to generate?
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />
          <Link
            to="/recipes"
            search={{
              ingridients: form.getValues("ingridients"),
              numberOfRecipes: form.getValues("numberOfRecipes"),
            }}
            className="flex justify-center"
          >
            <Button type="submit">Submit</Button>
          </Link>
        </form>
      </Form>
    </div>
  );
};

export default RecipesForm;
