print(r'''
                        ___
                        |  ~~--.
                        |%=@%%/
                        |o%%%/
                     __ |%%o/
               _,--~~ | |(_/ ._
            ,/'  m%%%%| |o/ /  `\.
           /' m%%o(_)%| |/ /o%%m `\
         /' %%@=%o%%%o|   /(_)o%%% `\
        /  %o%%%%%=@%%|  /%%o%%@=%%  \
       |  (_)%(_)%%o%%| /%%%=@(_)%%%  |
       | %%o%%%%o%%%(_|/%o%%o%%%%o%%% |
       | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |
       |  (_)%%=@%(_)%o%o%%(_)%o(_)%  |
        \ ~%%o%%%%%o%o%=@%%o%%@%%o%~ /
         \. ~o%%(_)%%%o%(_)%%(_)o~ ,/
          \_ ~o%=@%(_)%o%%(_)%~  _/
           `\_~~o%%%o%%%%%~~  _/'
              `--..__ __,,--'

''')
print("Welcome to the Pizza Game!")
repeat = input("Do you want to play? (yes/no) ")
while repeat.lower() == "yes":
    print("You're on an Island and you're hungry for pizza?: \n")
    first_choice = input(
        "You don't know the way. will you go Left or Right?\n").lower()

    while True:
        if first_choice == 'right':
            print('You realised you went the wrong way.\n')
            second_choice = input(
                "Do you want to walk to the other side or take a boat? (Walk / Boat)\n"
            ).lower()
            if second_choice == 'walk':
                print('You arrived at a pizzeria, the menu has three options')
                third_choice = input(
                    "Would you like a normal pizza, a pizza with mushrooms, or a pizza with pineapples?\n (Normal / Pineapples / Mushrooms)\n"
                ).lower()
                if third_choice == 'normal':
                    print(
                        'Game over! Your wife caught you eating pizza without her!'
                    )
                    break
                elif third_choice == 'mushrooms':
                    print('Game over! Mushrooms were poisoned!')
                    break
                elif third_choice == 'whiskey':
                    print('Fireworks and stuff\n')
                    print('YOU WIN!')
                    print('once in doubt, have whiskey!\n')
                    print('Fireworks and stuff')
                    quit()
                else:
                    print(
                        'Game over! An Italian saw you and stabbed you with a fork'
                    )
                    break
            else:
                print('Game over! You drowned')
                break
        else:
            print(
                "Game Over! You ran into your wife and she dragged you shopping =("
            )
            break

    repeat = input("Do you want to play again? (yes/no)").lower()
    if repeat.lower() == "no":
        print("Thank you for playing")
        quit()
