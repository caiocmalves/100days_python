import random

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

choice_pc = random.randint(0,2)
print(f"The PC choice is {choice_pc}")

if user >= 3 or user < 0:
    print("You typed n invalid number, you lose!")
elif user == 0 and choice_pc == 2:    
    print("You Win!")
elif user == 2 and choice_pc == 0:
    print("You lose.")
elif user > choice_pc:
    print("You win!")
elif user < choice_pc:
    print("You lose.")
elif user == choice_pc:
    print("It's a draw.")

    

#  0 for Rock, 1 for Paper, 2 for Scissors.