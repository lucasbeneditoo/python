# Exibe mensagem de boas-vindas
print("Bem-Vindo ao Calculator Python 2000!")

# Exibe opções do menu
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

# Lê a escolha do usuário
escolha = int(input("Escolha uma opção digitando seu número: "))

# Verifica a opção escolhida e realiza a operação correspondente
if escolha == 1:
    # Entrada dos dois números para soma
    val1 = float(input("Coloque um primeiro número para somar: "))
    val2 = float(input("Coloque um segundo número para somar: "))
    # Exibe o resultado da soma
    print("A soma dos dois números é igual a:", val1 + val2)

elif escolha == 2:
    # Entrada dos dois números para subtração
    val1 = float(input("Coloque um primeiro número para subtrair: "))
    val2 = float(input("Coloque um segundo número para subtrair: "))
    # Exibe o resultado da subtração
    print("A subtração dos dois números é igual a:", val1 - val2)

elif escolha == 3:
    # Entrada dos dois números para multiplicação
    val1 = float(input("Coloque um primeiro número para multiplicar: "))
    val2 = float(input("Coloque um segundo número para multiplicar: "))
    # Exibe o resultado da multiplicação
    print("A multiplicação dos dois números é igual a:", val1 * val2)

elif escolha == 4:
    # Entrada dos dois números para divisão
    val1 = float(input("Coloque um primeiro número para dividir: "))
    val2 = float(input("Coloque um segundo número para dividir: "))
    # Verifica se o divisor não é zero
    if val2 != 0:
        # Exibe o resultado da divisão
        print("A Dividisão dos dois números é igual a:", val1 / val2)
    else:
        # Mensagem de erro se tentar dividir por zero
        print("Não se pode dividir por zero!")

else:
    # Mensagem caso a opção escolhida seja inválida
    print("Opção Inválida!")
