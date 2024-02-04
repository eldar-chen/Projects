

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


# if position == 'A1':
#   line1[0] = 'X'
# elif position == 'A2':
#   line2[0] = 'X'
# elif position == 'A3':
#   line3[0] = 'X'
# elif position == 'B1':
#   line1[1] == 'X'
# elif position == 'B2':
#   line2[1] = 'X'
# elif position == 'B3':
#   line3[1] = 'X'
# elif position == 'C1':
#   line1[2] = 'X'
# elif position == 'C2':
#   line2[2] = 'X'
# elif position == 'C3':
#   line3[2] = 'X'
