

print("Welcome to treasure hunt!")

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("A~C, 1~3: \n") # Where do you want to put the treasure?

letter = position[0].upper()
abc = ["A","B","C"]
index = abc.index(letter)
number = int(position[1]) -1

map[number][index] = 'X'


print(f"{line1}\n{line2}\n{line3}")
