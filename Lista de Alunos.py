alunos = {}

while True:
    print("Bem vindo a lista de alunos!\n")
    print("1 - Adicionar aluno\n")
    print("2 - Listar Alunos\n")
    print("3 - Aprovados\n")
    print("4 - Média da turma\n")
    print("5 - Buscar nota de aluno\n")
    print("0 - Sair\n")
    while True:
        try:
            escolha = int(input("Selecione sua opção: "))
            print()
        except ValueError:
            print("Valor inválido! Tente novamente\n")
            continue
        if escolha in (1, 2, 3, 4, 5, 0):
            break
        else:
            print("Valor inválido! Tente novamente\n")

    if escolha == 1:
        nome = input("Digite o nome do aluno: ")

        while True:
            try:
                nota = float(input("\nDigite a nota do aluno: "))
                if(nota > 10):
                    print("Escreva uma nota que não ultrapasse a nota máxima (10)!")
                    continue
                break
            except ValueError:
                print("\nValor inválido! Tente novamente\n")

        alunos[nome.strip().title()] = nota

        print("\nLista atualizada com sucesso!\n")

    elif escolha == 2:
        print(", ".join(alunos), " ", sep=". \n")

    elif escolha == 3:
        for nome, nota in alunos.items():
            if nota > 5.9:
                print(f"Nome: {nome.strip().title()} | Nota: {nota:g}.\n")

    elif escolha == 4:
        media = sum(alunos.values()) / len(alunos)
        arredondado = round(media, 2)
        print(f"A media da turma é {arredondado:g}.\n")

    elif escolha == 5:
        busca = input("Escreva o nome de aluno para ver sua nota: ")
        for nome, nota in alunos.items():
            if nome.lower() == busca.lower().strip():
                print(f"\nNota de aluno {nome} é {nota:g}.\n")

    elif escolha == 0:
        print("Você saiu do programa!")
        break