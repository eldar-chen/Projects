print("Thank you for choosing Python Pizza Deliveries!")

# 🚨 Don't change the code above 👆
# Write your code below this line 👇
size = input("What size would you like? S, M or L \n") # What size pizza do you want? S, M, or L
add_pepperoni = input("Would you like to add pepperoni?\n") # Do you want pepperoni? Y or N
extra_cheese = input("would you like extra cheese?\n") # Do you want extra cheese? Y or N

bill = 0
pepperoni = 0
cheese = 0


if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25


if add_pepperoni == 'Y':
    if size == 'M' or size == "L":
        bill += 3
    else:
        pepperoni += 2

if extra_cheese == 'Y':
    bill += 1

print(f'Your final bill is: ${bill}.')


