"""
What we want to do today
    1. Build a simple menu on the console
    2. Work with Python's list and dict types
    3. Generate some random entities in the program (because we don't like to type too much)
    4. How to structure this small program :)

Problem statement:
    -- We want to manage a list of cities. Each city has a name, population, country and continent
What the program needs to do (requirements):
    1. Sort the cities
    2. Display the list of cities
    3. Search for a city (using partial, case-insensitve str matching)
    4. Add a city from the console
    5. Add a number of random cities to the list (the number is read from the console)
    6. Quit
"""


# --- Functions dealing with how cities are represented
def create_city(name: str, population: int, country: str, continent: str):
    # City represented as a Python list
    # return [name, population, country, continent]

    # City represented as a Python dict
    # dict is a key-to-value mapping where keys are unique
    return {"name": name, "pop": population, "country": country, "continent": continent}


def get_name(city) -> str:
    # for the list representation
    # return city[0]
    # for the dict representation
    return city["name"]


def get_population(city) -> str:
    # for the list representation
    # return city[1]
    # for the dict representation
    return city["pop"]


def get_country(city) -> str:
    # for the list representation
    # return city[2]
    # for the dict representation
    return city["country"]


def get_continent(city) -> str:
    # for the list representation
    # return city[3]
    # for the dict representation
    return city["continent"]


# --- Functions that implement program requirements

# --- User interface functions
# NOTE All print(), input() statements go here

def display_all_cities():
    pass


def start():
    while True:
        print("1. Display the list of cities")
        print("0. Quit")
        command = input(">")

        if command == 1:
            display_all_cities()
        elif command == 0:
            break
        else:
            print("Bad command or file name")


# start()

my_city = create_city("Tulcea", 65_000, "Romania", "Europe")
print(get_name(my_city), get_population(my_city))
