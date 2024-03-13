letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']

#x = 'caiocarvalho'

#shift = 5
#
def encode(x, shift):
    resultado_encode = []
    for i in x:
        for j in range(len(letras)):
                if i == letras[j]:
                    try:
                        resultado_encode.append(letras[j+shift])
                    except:
                        resultado_encode.append(letras[26-(j+shift)])
    print("A encriptação é: ", end='')
    for i in range(len(resultado_encode)):
         print(resultado_encode[i], end='')

###########################################################################
     #decode

#y= 'hfnthfxafqmt'
#shift = 5
#resultado_decode = []
def decode(x, shift):    
    resultado_encode =[]
    for i in x:
        for j in range(len(letras)):
                if i == letras[j]:
                    try:
                        resultado_encode.append(letras[j-shift])
                    except:
                        resultado_encode.append(letras[(j-shift)+26])
    print("A encriptação é: ", end='')
    for i in range(len(resultado_encode)):
         print(resultado_encode[i], end='')




