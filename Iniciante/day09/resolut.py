import os

bidders = {}
continua = True

def maior_bid(grupo_bids):
    max_bid = 0
    winner = ""    
    for bid in grupo_bids:
        bet_bid = grupo_bids[bid]
        if bet_bid > max_bid:
            max_bid = bet_bid
            winner = bid
    print(f"The winner is {winner} with a bid of ${max_bid}")        

while continua:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bidders[name] = price

    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continua = True
        maior_bid(bidders)
    elif should_continue == "yes":
        os.system("cls")
