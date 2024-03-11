import random

print("Welcome to the PyPassword Generator!")

lengh = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

senha = []
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']

for i in range(n_numbers):
    senha.append(random.randint(0,9))
for i in range(n_symbols):
    senha.append(random.choice(symbols))
while len(senha) < lengh:
    senha.append(random.choice(letters))

for i in range(n_symbols+n_numbers, len(senha)):
    if i % 2 == 0:
        senha[i] = senha[i].upper()
               

random.shuffle(senha)

for i in range(len(senha)):
    print(senha[i], end='')