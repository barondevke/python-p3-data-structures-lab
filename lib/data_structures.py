spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    foodList = []
    for x in spicy_foods:
        foodList.append(x['name'])

    print(foodList)


def get_spiciest_foods(spicy_foods):
    foodDict = []
    for x in spicy_foods:
        if x['heat_level'] > 5:
            foodDict.append(x)
    print(foodDict)


def print_spicy_foods(spicy_foods):
    for x in spicy_foods:
        print(
            f"{x['name']} ({x['cuisine']}) | Heat Level: { '🌶 ' * x['heat_level'] }")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass


def print_spiciest_foods(spicy_foods):
    pass


def get_average_heat_level(spicy_foods):
    pass


def create_spicy_food(spicy_foods, spicy_food):
    pass


print_spicy_foods(spicy_foods)
