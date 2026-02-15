print("Bem-Vindo ao Calculator Python 2000!\n")

while True:
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    print()

    escolha = int(input("Escolha uma opção digitando seu número: "))
    print()
    if escolha == 1:   
        while True:
            try:
                val1 = float(input("Coloque um primeiro número para somar: ")) 
                print()
                val2 = float(input("Coloque um segundo número para somar: "))
                print()
                print("A soma dos dois números é igual a:", val1 + val2)
                print()
                break

            except ValueError:
                print("Valor inválido! Tente novamente.\n")

    elif escolha == 2:
        while True:
            try:
                val1 = float(input("Coloque um primeiro número para subtrair: "))
                print()
                val2 = float(input("Coloque um segundo número para subtrair: "))
                print()
                print("A subtração dos dois números é igual a:", val1 - val2)
                print()
                break

            except ValueError:
                print("Valor inválido! Tente novamente.\n")

    elif escolha == 3:
        while True:
            try:
                val1 = float(input("Coloque um primeiro número para multiplicar: "))
                print()
                val2 = float(input("Coloque um segundo número para multiplicar: "))
                print()
                print("A multiplicação dos dois números é igual a:", val1 * val2)
                print()
                break

            except ValueError:
                print("Valor inválido! Tente novamente.\n")

    elif escolha == 4:
        while True:
            try:
                val1 = float(input("Coloque um primeiro número para dividir: "))
                print()
                val2 = float(input("Coloque um segundo número para dividir: "))
                print()
                if val2 != 0:
                    print("A Divisão dos dois números é igual a:", val1 / val2)
                    print()
                    break
                else:
                    print("Não se pode dividir por zero!\n")
            except ValueError:
                print("Valor inválido! Tente novamente.\n")

    elif escolha == 0:
        print("Você saiu do programa.")
        break
    
    else:
        print("Opção Inválida!\n")