print("Bem-Vindo ao Caculator Python 2000!")

print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

escolha = int(input("Escolha uma opção digitando seu número: "))

if escolha == 1:
    val1 = float(input("Coloque um primeiro número para somar: "))
    val2 = float(input("Coloque um segundo número para somar: "))
    print("A soma dos dois números é igual a:", val1 + val2)

elif escolha == 2:
    val1 = float(input("Coloque um primeiro número para subtrair: "))
    val2 = float(input("Coloque um segundo número para subtrair: "))
    print("A subtração dos dois números é igual a:", val1 - val2)

elif escolha == 3:
    val1 = float(input("Coloque um primeiro número para multiplicar: "))
    val2 = float(input("Coloque um segundo número para multiplicar: "))
    print("A multiplicação dos dois números é igual a:", val1 * val2)

elif escolha == 4:
    val1 = float(input("Coloque um primeiro número para dividir: "))
    val2 = float(input("Coloque um segundo número para dividir: "))
    if val2 != 0:
        print("A Dividisão dos dois números é igual a:", val1 / val2)
    else:
        print("Não se pode dividir por zero!")
else:
    print("Opção Inválida!")