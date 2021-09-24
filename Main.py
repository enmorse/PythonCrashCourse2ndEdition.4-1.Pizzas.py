# Think of at least three kinds of your favorite pizza, or category
# of food, food type, or type of food. Store these in a list, and then
# use a for loop to print the name of each item in the list.

# Modify you for loop to print a sentence using the name
# of the items instead of printing just the name of the
# items. For each item you should have one line of
# output containing a simple statement like "I like
# peaches."

# Add a line at the end of your program, outside the for
# loop, that states how much you like the food, category
# of food, food type, or type of food. The output
# should consist of three or more lines about the kinds
# of food you like and then an additional sentence, such
# as "I really love peaches!"

favorite_fruits = ["blueberries", "cherries", "peaches"]

for fruit in favorite_fruits:
    print(f"I like {fruit.title()}.")
print(f"I like {favorite_fruits[0].title()},"
      f"\nI like {favorite_fruits[1].title()},"
      f"\nbut nothing compares to {favorite_fruits[2].title()},"
      f"\nI really love {favorite_fruits[2].title()}!")
