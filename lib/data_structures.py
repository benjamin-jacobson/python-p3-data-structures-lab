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
    return [i['name'] for i in spicy_foods]

def get_spiciest_foods(spicy_foods):
    x = [i if i['heat_level'] >5 else None for i in spicy_foods]
    x.remove(None)
    return x

def print_spicy_foods(spicy_foods):
    for j in spicy_foods:
        print(f"{j['name']} ({j['cuisine']}) | Heat Level: {'🌶'* j['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass

# running
print(get_names(spicy_foods))
print(get_spiciest_foods(spicy_foods))
print_spicy_foods(spicy_foods)