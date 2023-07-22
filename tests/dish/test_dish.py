from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
from pytest import raises


def test_dish():
    with raises(ValueError):
        dish = Dish("lasanha berinjela", -10.0)
    dish = Dish("Pizza", 10.0)
    assert dish.name == "Pizza"

    dish1 = Dish("Pizza", 10.0)
    dish2 = Dish("Pizza", 10.0)
    assert hash(dish1) == hash(dish2)

    dish3 = Dish("Pizza", 10.0)
    dish4 = Dish("Burger", 10.0)
    assert hash(dish3) != hash(dish4)

    assert dish1 == dish2

    assert dish1 != dish4

    assert repr(dish1) == "Dish('Pizza', R$10.00)"

    try:
        dish = Dish("Pizza", "10.0")
    except TypeError as e:
        assert str(e) == "Dish price must be float."

    try:
        dish = Dish("Pizza", -10.0)
    except ValueError as e:
        assert str(e) == "Dish price must be greater then zero."

    ingredient1 = Ingredient("Tomato")
    dish.add_ingredient_dependency(ingredient1, 2)
    assert dish.recipe.get(ingredient1) == 2

    ingredient1.restrictions = {"vegan"}
    ingredient2 = Ingredient("Cheese")
    ingredient2.restrictions = {"vegetarian"}
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)
    assert dish.get_restrictions() == {"vegan", "vegetarian"}

    assert dish.get_ingredients() == {ingredient1, ingredient2}

    dish5 = Dish("Burger", 15.0)
    ingredient3 = Ingredient("Bread")
    ingredient4 = Ingredient("Beef")
    ingredient4.restrictions = {"halal"}
    dish5.add_ingredient_dependency(ingredient3, 2)
    dish5.add_ingredient_dependency(ingredient4, 1)
    assert dish5.name == "Burger"
    assert dish5.price == 15.0
    assert dish5.recipe == {ingredient3: 2, ingredient4: 1}
    assert dish5.get_restrictions() == {"halal"}
    assert dish5.get_ingredients() == {ingredient3, ingredient4}
