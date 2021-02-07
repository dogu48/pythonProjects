# print("hello world")
#
# for i in range(1, 13):
#     print("No. {} squared is {} and cubed is {:4}" .format(i, i ** 2, i ** 3))

# age = int(input("How old are you? "))
# if 16 <= age <= 65:
#     print("Have a good day at work")
#
# day = "Monday"
# temperature = 30
# raining = True
#
# if day == "Saturday" and temperature> 27 and not raining:
#     print("Go swimming")
#
#
# parrot = "Norwegian Blue"
#
# letter = input("Enter a character: ")
#
# if letter in parrot:
#     print("{} is in {}".format(letter, parrot))
# else:
#     print("I don't need that letter")

# activity = input("What would you like to do today? ")
# if "cinema" not in activity.casefold(): #casefold lowercase yapar
#     print("But I want to go to the cinema")


# name = input("What is your name? ")
# age = int(input("What is your age? "))
#
# if 18 <= age < 31:
# if age in range(16, 66):
#     print("Welcome {} ".format(name))
# else:
#     print("Sorry")


# number = "9,223;372:036 854,775;807"
# seperators = ""
# for char in number:
#     if not char.isnumeric():
#         seperators+= char
#
# print(seperators)

# number = input("Please enter a series of numbers, using any separators you like: ")
# seperators = ""
# for char in number:
#     if not char.isnumeric():
#         seperators+= char
#
# print(seperators)

# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
#
# for char in quote:
#     if char.isupper():
#        print(char)

# for i in range(1, 21):
#     print("i is now {}".format(i))
#
# for i in range(0, 10, 2):
#     print("i is now {}".format(i))

# for i in range(10, 0, -2):
#     print("i is now {}".format(i))

# for i in range (0, 101):
#     if (i % 7) == 0:
#         print(i)
#
# for i in range(0,101,7):
#     print(i)

# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#
# for item in shopping_list:
#     if item == "spam":
#         continue
#     print("Buy " + item)

# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# item_to_find = "ahmet"
# found_at = None
#
# #for index in range(6):
# for index in range (len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
#
# # if item_to_find in shopping_list:
# #     found_at = shopping_list.index(item_to_find)
#
# if found_at is not None:
#     print("Item found at position {}".format(found_at))
# else:
#     print("{} not found".format(item_to_find))


# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

# available_exists = ["north", "south", "east", "west"]
#
# chosen_exists = ""
# while chosen_exists not in available_exists:
#     chosen_exists = input("Please choose a direction: ")
#     if chosen_exists.casefold() == "quit":
#         print("Game over")
#         break
#
# print("helal")
# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break


for i in range(0,21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
