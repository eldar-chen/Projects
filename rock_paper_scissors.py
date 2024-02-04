rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#Write your code below this line 👇
import random
print('''
0. - Rock
1. - Paper
2. - Scissors0
      
''')

while True:
    try:
        player_choice = int(input("Please enter: 0 for rock, 1 for paper, or 2 for scissors\n"))
        if 0 <= player_choice <= 2:
            break  # If the input is successfully converted to an integer and within the valid range, exit the loop
        else:
            print("Invalid input. Please enter a valid number 0, 1, or 2.")
    except ValueError:
        print("Invalid input. Please enter a valid number 0, 1, or 2.")
computer_choice = random.randint(0,2)

images = [rock, paper, scissors]


print(images[player_choice])
print("Computer Choice:")
print(images[computer_choice])

if player_choice >= 3 or player_choice < 0:
    print("you chose an invalid number, you lose!")
elif player_choice == 2 and computer_choice == 0:
    print("You lose")
elif computer_choice == 2 and player_choice == 0:
    print("You Win!")
elif player_choice > computer_choice:
    print("You win!")
elif computer_choice > player_choice:
    print("You Lose!")
elif player_choice == computer_choice:
    print("Its a draw!")


