# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 18:45:48 by joslopez          #+#    #+#              #
#    Updated: 2023/04/12 17:57:02 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ["avocado", "arugugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def print_recipe(recipe_name):
    if recipe_name in cookbook:
        recipe = cookbook[recipe_name]
        print(f"Recipe for {recipe_name}:")
        print(f"\tIngredients list: {recipe['ingredients']}")
        print(f"\tTo be eaten for {recipe['meal']}.")
        print(f"\tTakes {recipe['prep_time']} minutes of cooking.")
        print("\n")
    else:
        print(f"{recipe_name} is not in the cookbook.")

def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print(f"{recipe_name} recipe deleted from the cookbook.")
    else:
        print(f"{recipe_name} is not in the cookbook.")
        
def print_cookbook():
    for recipe_name in cookbook.keys():
        print_recipe(recipe_name)
        print("")
        
def add_recipe():
    name = input("Enter recipe name: ")
    count_empty_lines = 0
    print("Enter list of ingredients:")
    item = []
    while count_empty_lines < 1:
        ingredientes = input()
        if ingredientes == "":
            count_empty_lines += 1
        else:
            count_empty_lines = 0
            item.append(ingredientes)
    meal = input("Enter meal type: ")
    prep_time = int(input("Enter preparation time in minutes: "))
    recipe = {"ingredients": item, "meal": meal, "prep_time": prep_time}
    cookbook[name] = recipe
    print(f"{name} recipe added to the cookbook.")
    
def print_options():
    print("List of available options:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit")
    print("\n")
    
print("Welcome to the Python Cookbook!")
print_options()

while True:
    #print_options()
    option = input("Please select an option: \n")
    
    if option == "1":
        print("\n")
        add_recipe()
        print("\n")
    elif option == "2":
        print("\n")
        recipe_name = input("Please enter a recipe name to delete: \n")
        print("\n")
        delete_recipe(recipe_name)
    elif option == "3":
        print("\n")
        recipe_name = input("Please enter a recipe name to get its details: \n")
        print("\n")
        print_recipe(recipe_name)
    elif option == "4":
        print("\n")
        print_cookbook()
        print("\n")
    elif option == "5":
        print("\n")
        print("Cookbook closed. Goodbye !")
        break
    else:
        print("\n")
        print("Sorry, this option does not exist.")
        print_options()