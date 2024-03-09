import random

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

choice_pc = random.randint(0,2)

if user == choice_pc:
    print(f"The PC choice is {choice_pc}")
    print("It's a draw!")
elif user == 0 and choice_pc == 1:
    print(f"The PC choice is {choice_pc}")
    print("You lose.")
elif user == 0 and choice_pc == 2:
    print(f"The PC choice is {choice_pc}")
    print("You Win!")
elif user == 1 and choice_pc == 0:
    print(f"The PC choice is {choice_pc}")
    print("You Win.")
elif user == 1 and choice_pc == 2:
    print(f"The PC choice is {choice_pc}")
    print("You lose!")
elif user == 2 and choice_pc == 0:
    print(f"The PC choice is {choice_pc}")
    print("You lose.")
elif user == 2 and choice_pc == 1:
    print(f"The PC choice is {choice_pc}")
    print("You Win!")

#  0 for Rock, 1 for Paper, 2 for Scissors.