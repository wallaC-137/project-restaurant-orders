from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


def test_ingredient():
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("farinha")
    assert hash(ingredient1) == hash(ingredient2)

    ingredient3 = Ingredient("farinha")
    ingredient4 = Ingredient("bacon")
    assert hash(ingredient3) != hash(ingredient4)

    ingredient5 = Ingredient("farinha")
    ingredient6 = Ingredient("farinha")
    assert ingredient5 == ingredient6

    ingredient7 = Ingredient("farinha")
    ingredient8 = Ingredient("bacon")
    assert ingredient7 != ingredient8

    ingredient9 = Ingredient("farinha")
    assert repr(ingredient9) == "Ingredient('farinha')"

    ingredient10 = Ingredient("farinha")
    assert ingredient10.name == "farinha"

    ingredient11 = Ingredient("queijo mussarela")
    assert ingredient11.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    ingredient12 = Ingredient("farinha")
    assert isinstance(ingredient12, Ingredient)
