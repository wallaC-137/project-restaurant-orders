import csv

from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        ingredients = {}

        with open(source_path, newline="") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)

            for row in reader:
                self._add_dish(row, ingredients)

    def _add_dish(self, row, ingredients):
        dish_name, dish_price, ingredient_name, ingredient_quantity = row

        dish_price = float(dish_price)
        ingredient_quantity = float(ingredient_quantity)

        if ingredient_name not in ingredients:
            ingredient = Ingredient(ingredient_name)
            ingredients[ingredient_name] = ingredient
        else:
            ingredient = ingredients[ingredient_name]

        dish = next((d for d in self.dishes if d.name == dish_name), None)
        if not dish:
            dish = Dish(dish_name, dish_price)
            self.dishes.add(dish)

        dish.add_ingredient_dependency(ingredient, ingredient_quantity)
