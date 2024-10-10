"""
What do we practice today?
    - Write a menu-based program
    - Practice Python list, dict types
    - How to represent program entities? -- list. vs dict
    - How to structure the program

Problem statement
    -- Manage a list of cities. Each city has a name, population and a county
Program requirements
    -- Sort them by any of their features (name, pop or county)
    -- Add a city from the console
    -- Generate some random cities :)
    -- Search for a city, using case-insensitive partial string matching
    -- Exit the program
"""


# --- Functions that deal with how a city is represented

# A city represented using a Python list
# my_city = ["Constanta", 200_000, "Constanta"]

# A dict is a set of key-to-value mappings; keys must be unique, values not necesarely
# A city represented using a Python dict
# my_city = {"name": "Braila", "population": 150_000, "county": "Braila"}


def create_city(name: str, population: int, county: str):
    # list representation
    # return [name, population, county]
    # dict representation
    return {"name": name, "population": population, "county": county}


def get_name(city) -> str:
    # list representation
    # return city[0]
    # dict representation
    return city["name"]


def get_population(city) -> int:
    # return city[1]
    return city["population"]


def get_county(city) -> str:
    # return city[2]
    return city["county"]


def to_str(city) -> str:
    return get_name(city) + " with population of " + str(get_population(city)) + " is in " + get_county(city)


# --- Functions that implement program requirements


# --- User interface functions
# NOTE The only place where we are allowed to write print(), input() statements

# my_city = create_city("Braila", 150_000, "Braila")
# print(get_name(my_city), get_population(my_city))
# print(to_str(my_city))

def start():
    while True:
        print("1. Show all cities")
        print("0. Exit")

        command = input(">")

        if command == 1:
            pass
        elif command == 0:
            # return
            # exit(0)
            break
        else:
            print("Bad command or file name")


# print(locals())
start()