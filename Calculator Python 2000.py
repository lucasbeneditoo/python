import math

print("Bem-Vindo ao Calculator Python 2000!\n")

def conferir_escolha_menu(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido! Tente novamente.\n")

def fazer_a_conta(escolha, mensagem):
    while True:
        try:
            quantidade = int(input(mensagem))
            print()
            if quantidade < 1:
                print("Você precisa digitar pelo menos 1 número.\n")
                continue
            elif escolha in (2, 4, 5) and quantidade < 2:
                print("Para subtração ou divisão, é preciso pelo menos 2 números.\n")
                continue
            break
        except ValueError:
            print("\nValor inválido! Tente novamente.\n")
    resultado = []
    for i in range(quantidade):
        while True:
            try:
                n = float(input(f"Digite o {i+1}º número: "))
                print()
                if escolha == 4 and i > 0 and n == 0:
                    print("\nNão dá para dividir por zero! Tente outro número.\n")
                    continue
                resultado.append(n)
                break
            except ValueError:
                print("\nValor inválido! Digite um número válido.\n")
    if escolha == 1:  
        total = sum(resultado)
    elif escolha == 2: 
        total = resultado[0]
        for n in resultado[1:]:
            total -= n
    elif escolha == 3:  
        total = math.prod(resultado)
    elif escolha == 4: 
        total = resultado[0]
        for n in resultado[1:]:
            total /= n
    elif escolha == 5:
        total = sum(resultado) / len(resultado)
    print(f"O resultado é {total:g}\n")

while True:
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Média")
    print("0 - Sair")
    print()
    while True:
        escolha = conferir_escolha_menu("Escolha uma opção: ")
        if escolha in (1, 2, 3, 4, 5, 0):
            break
        else:
            print("Opção Inválida! Tente novamente.\n")
    print()
    if escolha == 1:  
        fazer_a_conta(escolha, "Quantos números você quer somar: ")
    elif escolha == 2:
        fazer_a_conta(escolha, "Quantos números você quer subtrair: ")
    elif escolha == 3:
        fazer_a_conta(escolha, "Quantos números você quer multiplicar: ")
    elif escolha == 4:
        fazer_a_conta(escolha, "Quantos números você quer dividir: ")
    elif escolha == 5:
        fazer_a_conta(escolha, "Quantos números você quer para fazer a média: ")
    elif escolha == 0:
        print("Você saiu do programa.")
        break