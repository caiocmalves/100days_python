import regras

print('Bem vindo ao software de codificação caesar!')

programa = True
while programa:
    tipo_encript = input("Digite 'encode' para encriptar ou digite 'decode' para decodificar: ").lower().strip()
    if tipo_encript == 'encode' or tipo_encript == 'decode':   
        msg = input("Digite sua mensagem: ").lower().strip()
        shift_number = int(input("Digite o numero de encriptação: "))
        if tipo_encript == 'encode':
            regras.encode(msg, shift_number)
        else:
            regras.decode(msg, shift_number)    
        print()
        print()
        continua = 'sim'
        while continua == 'sim':
            continua = input("Para rodar o programa novamente digite 'sim', caso queira finalizar, digite 'nao': \n").lower().strip()
            if continua == 'sim' or continua == 'nao':
                if continua == 'sim':
                    programa
                    continua = 'qualquercoisa'
                else:
                    programa = False
                    continua = 'qualquercoisa'
            else:
                print('Você digitou errado, favor tentar novamente.')
                continua = 'sim'
            

    else:
        print('Você digitou a palavra incorreta, tente novamente.')

print('Obrigado por usar o programa, até a próxima!')