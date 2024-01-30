print("Hello, Wleome to my Tip Calculator")

## If the bill was $150, split between 5 people, with 10,12 or 15% tip. 
# Bill input
bill = float(input("Please enter the sum $"))
## Round the result to 2 decimal points
# tip input
tip = float(input("please enter desierd tip: 10,12 or 15%: Note do not type '%' signs "))
# split choice input
split_choice = float(input("How many people will be paying? "))
# Calculate the tip ammount

tip_sum = (bill * tip) / 100
total = bill + tip_sum
final_bill = total / split_choice
final_bill = round(final_bill, 2)

print(f"Each person should pay: ${final_bill:.2f}")
