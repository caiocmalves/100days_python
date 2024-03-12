import random
from letras import word_list

palavra_escolhida = random.choice(word_list)
tamanho_palavra = len(palavra_escolhida)
vidas = 6
fim_do_jogo = False
print('Bem vindo ao jogo de FORCA! Você tem 6 vidas. Vamos começar!')

while fim_do_jogo == False:
    letra = input('Adivinhe uma letra: ')
    for i in range(len(palavra_escolhida)):
        print("_", end=' ')
    if letra not in palavra_escolhida:
        vidas =- 1
        print(f'Você chutou a letra {letra}, esta letra não tem na palvra. Perdeu uma vida.')
        print(f'Agora você tem {vidas} vidas')
    

    if vidas == 0:
        fim_do_jogo = True
        print('Você perdeu!')
      
    
    #if letra in palavra_escolhida:
    #    print(f'Você chutou a letra {letra}, parabéns!')
     #   for i in len(palavra_escolhida):
      #      if palavra_escolhida[i] == letra:


