print("Welcome to Treasure Island.")
print("Your mission is to find the trasure.")
direction = input("You're at a cross road. Where do you want to go?\n     Type 'left' or 'right'\n")

if direction == "left":
    action = input("You've come to a Lake. There is an Island in the middle of the lake.\n     Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if action == "wait":
        color = input("You arrive at the island unharmed. There is a house with 3 doors\n    One red, one yellow and one blue. Which color do you choose?\n")
        if color == "yellow":
            print("You found the treasure! You win!")
        elif color == "red":
            print("It's a room full of fire. Game over.")
        else:
            print("You enter a room of beasts. Game over.")
    else:
        print("You get attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game Over")