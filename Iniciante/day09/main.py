import os

print('Welcome to the bid program')

otherBidder = "yes"
bidders = {}

while otherBidder == "yes":
    nome = input("What is your name? ").strip()
    preco = float(input('What is your bid? $').strip())
    bidders[nome] = preco

    otherBidder = input("Are there any other bidders? Type 'yes' or 'no'\n").strip().lower()
    if otherBidder == "yes":
       os.system("cls")
print()
print(f'The winner is {max(bidders,key=bidders.get)} with a bid of ${bidders[max(bidders,key=bidders.get)]:.2f}')

