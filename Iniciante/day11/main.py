import random



def iniciarJogo():
    dealer.append(random.choice(cards))
    dealer.append(random.choice(cards))
    player.append(random.choice(cards))
    player.append(random.choice(cards))
    definirCarta(player)
    definirCarta(dealer)
    
def contagemMao(player,dealer):
    print(f"Suas cartas: {player}, sua pontuação atual: {sum(player)}")
    print(f"Primeira carta do dealer: {dealer[0]}")


def definirCarta(lista):
    for i in range(len(lista)):
        if lista[i] == "valete" or lista[i] == "dama" or lista[i] == "rei":
            lista[i] = 10
    for i in range(len(lista)):
        if lista[i] == "as":
            lista[i] = 11
            if sum(lista) > 21:
                lista[i] = 1    

def conferirJogo(player,dealer):
    if sum(player) > 21:
            print(f"Sua mão final: {player}, sua pontuação final: {sum(player)}")
            print(f"Mão final do dealer: {dealer}")
            print("Você passou de 21. Você perdeu! :()")
    elif sum(dealer) > 21 and sum(player) <= 21:
            print(f"Sua mão final: {player}, sua pontuação final: {sum(player)}")
            print(f"Mão final do dealer: {dealer}")
            print("O dealer passou de 21. Você ganhou! :))")
    elif sum(player) <= 21 and sum(dealer) < sum(player):
            print(f"Sua mão final: {player}, sua pontuação final: {sum(player)}")
            print(f"Mão final do dealer: {dealer}")
            print("Parabéns, Você ganhou! :))")
         


cards = [2,3,4,5,6,7,8,9,10,"valete","dama","rei","as"]
dealer = []
player = []
play = "sim"
maisUmaCarta = 'sim'
play = input("Você quer jogar Blackjack? Digite 'sim' ou 'não':  ").lower().strip()


while play == "sim":
    iniciarJogo()
    contagemMao(player,dealer)
    print()
    while maisUmaCarta == "sim":
        maisUmaCarta =  input("Digite 'sim' para pegar mais uma carta ou digite 'não' para passar a vez: ").lower().strip()
        if maisUmaCarta == "sim":
            player.append(random.choice(cards))
            definirCarta(player)
            print()
            contagemMao(player,dealer)
            conferirJogo(player,dealer)
            


        else:
            definirCarta(player)
            contagemMao(player,dealer)
            conferirJogo(player,dealer)
        maisUmaCarta = "não"

    play = input("Você quer jogar Blackjack? Digite 'sim' ou 'não':  ").lower().strip()            
