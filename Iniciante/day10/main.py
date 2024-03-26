import calc

print("Bem vindo a calculadora!")

operadores = {
    "+": calc.soma,
    "-": calc.subtrai,
    "*": calc.multiplica,
    "/": calc.divide
}

continuar = True
first_num = float(input("Qual é o primeiro número? :" ))

for i in operadores:
    print(i)


while continuar:    
    operacao = input("Escolha uma operação: ").strip()
    second_num = float(input("Qual é o próximo número? : "))
    operador = operadores[operacao]
    resolucao = operador(first_num, second_num)
    print(f"{first_num} {operacao} {second_num} = {resolucao}")

    sec = input(f"Digite 'y' para continuar a calcular com {resolucao}, ou digite 'n' para começar um novo calculo: ").strip().lower()
    if sec == 'y':
        first_num = resolucao
    else:
        continuar = False