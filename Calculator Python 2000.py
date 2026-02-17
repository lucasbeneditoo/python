print("Bem-Vindo ao Calculator Python 2000!\n")

def conferir_int_usuario(mensagem):
    while True:
        try:
            return int(input(mensagem))
        
        except ValueError:
            print("Valor inválido! Tente novamente.\n")

def conferir_float_usuario(mensagem):
    while True:
        try:
            return float(input(mensagem))
        
        except ValueError:
            print("Valor inválido! Tente novamente.\n")
        

while True:
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    print()

    while True:
        escolha = conferir_int_usuario("Escolha uma opção: ")
        if escolha in (1, 2, 3, 4, 0):
            break

        else:
            print("Opção Inválida! Tente novamente.\n")

    print()
    
    if escolha == 1:   
        val1 = conferir_float_usuario("Coloque um primeiro número para somar: ")
        
        print()

        val2 = conferir_float_usuario("Coloque um segundo número para somar: ")

        print()

        print("A soma dos dois números é igual a:", val1 + val2)

        print()

    elif escolha == 2:
        val1 = conferir_float_usuario("Coloque um primeiro número para subtrair: ")

        print()

        val2 = conferir_float_usuario("Coloque um segundo número para subtrair: ")

        print()

        print("A subtração dos dois números é igual a:", val1 - val2)

        print()

    elif escolha == 3:
        val1 = conferir_float_usuario("Coloque um primeiro número para multiplicar: ")

        print()

        val2 = conferir_float_usuario("Coloque um segundo número para multiplicar: ")

        print()

        print("A multiplicação dos dois números é igual a:", val1 * val2)

        print()

    elif escolha == 4:
        val1 = conferir_float_usuario("Coloque um primeiro número para dividir: ")
    
        print()

        val2 = conferir_float_usuario("Coloque um segundo número para dividir: ")

        print()

        if val2 != 0:
            print("A Divisão dos dois números é igual a:", val1 / val2)

            print()

        else:
            print("Não se pode dividir por zero!\n")


    elif escolha == 0:
        print("Você saiu do programa.")
        break
