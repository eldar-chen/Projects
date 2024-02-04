import random
print("\n\nWelcome to Beer lottery!!\nthe super fair way to decide who'll be paying for beer\n\n")
names_string = input("Please enter the names:\n")
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

length = len(names)
buyer = names[random.randint(0,length - 1)]
print(f'\n{buyer} is going to buy the beer today!\n')
