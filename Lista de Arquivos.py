def adicionar_item(item):
    with open("tarefas.txt", "a") as arquivo:
        arquivo.write(item + "\n")
        print("\nArquivo adicionado com sucesso!\n")

def ler_lista():
    try:
        with open("tarefas.txt", "r") as arquivo:
            print()
            for i, item in enumerate(arquivo, 1):
                print(i, item.strip())
            print()

    except FileNotFoundError:
        print("\nArquivo não encontrado!\n")


def excluir_item():
    try:
        with open("tarefas.txt", "r") as arquivo:
            lista = arquivo.readlines()
        if not lista:
            print("Não tem tarefas!")
            return
        print()
        for i, item in enumerate(lista, 1):
            print(i, item.strip())
        print()

        item = int(input("Digite o número da tarefa que você quer excluir: "))

        if 0 < item <= len(lista):
            lista.pop(item-1)

        else:
            print("Valor inválido!")
            return

        with open("tarefas.txt", "w") as arquivo:
            for linha in lista:
                arquivo.write(linha)

    except FileNotFoundError:
        print("\nArquivo não encontrado!\n")
        
while True:
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("0 - Sair")

    while True:
        try:
            escolha = int(input("Selecione sua opção: "))
        except ValueError:
            print("Valor inválido! Tente novamente\n")
            continue
        if escolha in [0, 1, 2, 3]:
            break
        else: print("Valor inválido! Tente novamente\n")


    if escolha == 1:
        item = input("\nDigite a tarefa: ")
        adicionar_item(item)

    elif escolha == 2:
        ler_lista()

    elif escolha == 3:
        excluir_item()


    elif escolha == 0:
        print("Você saiu do programa!")
        break