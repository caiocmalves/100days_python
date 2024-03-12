import random
from letras import word_list

palavra_escolhida = random.choice(word_list)
tamanho_palavra = len(palavra_escolhida)
vidas = 6
fim_do_jogo = False
print('Bem vindo ao jogo de FORCA! Você tem 6 vidas. Vamos começar!')
adivinhando = []
for i in range(len(palavra_escolhida)):
    adivinhando.append("_")


while fim_do_jogo == False:
    letra = input('Adivinhe uma letra: ').lower()
    if letra not in palavra_escolhida:
        vidas -= 1
        print(f'Você chutou a letra {letra}, esta letra não tem na palavra. Perdeu uma vida.')
        print(f'Agora você tem {vidas} vidas')
    else:
        for i in range(len(palavra_escolhida)):
            if letra == palavra_escolhida[i]:
                adivinhando[i] = letra 
    for i in range(len(adivinhando)):
        print(adivinhando[i], end=' ')
    print()
    

    if vidas == 0:
        fim_do_jogo = True
        print('Você perdeu!')
        print(f'A palavra era {palavra_escolhida}')
    print()      

