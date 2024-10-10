"""
    1. Bulid a simple menu on the console
    2. Work with list and dicts types
    3. Generate some random entities in the program (for not typing that much)
    4. How to structure this small program

Problem statement:
    - We want to manage a list of cities. Each city has a name, population, country and continent
      Requirments:
        1.  Sort the cities
        2. Display the list of cities
        3. Search for a city (using partial, case-insensitive str matching)
        4. Add a city from the console
        5. Add a number of random cities to the list (the number is read from the console)
        6. Quite
        
"""

# Functions dealing how cities are represented



# Functions that implement program requirments



# Use interface functions
# NOTE ALL print() , input() statements go here

def create_city(name, population, country, continent):
    # city represented as a list
    return [name, population, country, continent]
        # or
    # city represented as a dict (dict is a key-to-value mapping where keys are unique)
    # return { "name" : name, "pop" : population, "country" : country, "continent" : continent }

def get_name(city):
    # for list representation
    return city[0]
    
    # for dict representation
    # return city["name"]

def get_population(population):
    # for list representation
    return population[1]
    
    # for dict representation
    # return population["name"] 

def get_country(country):
    # for list representation
    return country[2]
    
    # for dict representation
    # return country["name"]
    
def get_continent(continent):
    # for list representation
    return continent[3]
    
    # for dict representation
    # return continent["name"]

def to_str(city):
    return get_name(city) + " with a population of " + str(get_population(city)) + " is in " + get_country(city) + ", " + get_continent(city) + "."

def add_city(city_list):
    print("Adding a new city")
    name = input("City name is ")
    
    while True:
        try:
            pop = int(input("City population is "))
            break  # If we get to this point, it means there was no error. Try it!
        except ValueError:
            print("Population must be an integer")
    
    country = input("Country is ")
    continent = input("Continent is ")
    
    #TODO What to do with duplicate cities?
    new_city = create_city(name, pop, country, continent)
    city_list.append(new_city)

def display_all_cities(city_list):
    for city in city_list:
        print(to_str(city))

def start():
    
    # NOTE We don't want to start with an empty list, so let's add something
    
    # This is where we keep all the cities
    # It's not a global variable
    
    city_list = []
    
    city_list.append(create_city("Roman", 20_000, "Romania", "Europe"))
    city_list.append(create_city("Ploiesti", 80_000, "Romania", "Europe"))
    
    while True:
        print("1. Display the list of cities")
        print("2. Add a city")
        print("0. Quit")
        
        command = input("Enter a number ").strip()

        if command == "1":
            # We want to add a function for each  requirment
            # This makes the main loop easier to understand
            display_all_cities(city_list)
        elif command == "2":
            add_city(city_list)
        elif command == "0":
            return
        else:
            print("Bad command or file name")
        
start()

# my_city = create_city("Roman", 17_000, "Romania", "Europe")
# print(get_name(my_city), get_population(my_city), get_country(my_city), get_continent(my_city))
# print(to_str(my_city))