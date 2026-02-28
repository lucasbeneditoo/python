from colorama import init, Fore, Style
init(autoreset=True)

produtos = []

def adicionar_produtos(nome, preco, quantidade): #Opção 1: Adicionar produtos.
    produto = {"nome": nome.strip().title(), "preco": preco, "quantidade": quantidade}

    produtos.append(produto)

def remover_produtos(): #Opção 2: Excluir produtos.

    if not listar_produtos():
        return

    while True:
        try:
            numero_produto = int(input("\nQual produto deseja remover? (Selecione pelo número do produto | Selecione '0' para sair): "))

        except ValueError:
            print(Fore.RED + "\nValor inválido! Tente novamente.")
            continue

        if 0 < numero_produto <= len(produtos):
            produtos.pop(numero_produto-1)
            break

        elif numero_produto == 0:
            return

        else:
            print(Fore.RED + "\nValor inválido! Tente novamente.")
            continue

def modificar_produto(): #Opção 3: Modificar produtos.

    if not listar_produtos():
        return
    
    while True:
        try:
            numero_produto = int(input("\nQual produto você quer modificar? (Selecione o número do produto | Selecione '0' para sair): "))
        
        except ValueError:
            print(Fore.RED + "\nValor inválido! Tente novamente.")
            continue

        if 0 < numero_produto <= len(produtos):
            break

        elif numero_produto == 0:
            return  

        else:
            print(Fore.RED + "\nValor inválido! Tente novamente.")
            continue

    produto_modificado = produtos[numero_produto - 1]

    while True:
        try:
            opcao = int(input(f"\n1. Nome: {produto_modificado['nome']}\n2. Preço: R${produto_modificado['preco']:.2f}\n3. Quantidade {produto_modificado['quantidade']}.\n\nSelecione o que você quer mudar (Selecione o número da opção '1, 2, 3' | Selecione '0' para sair): "))
            if opcao in (0, 1, 2, 3):
                break
            else:
                print(Fore.RED + "\nValor inválido! Tente novamente.")
        except ValueError:
            print(Fore.RED + "\nValor inválido! Tente novamente.")

    if opcao == 1:
        while True:
            try:
                novo_nome = input("Digite o novo nome do produto: ")
                break

            except ValueError:
                print(Fore.RED + "\nValor inválido! Tente novamente.")

        produto_modificado['nome'] = novo_nome.strip().tittle()
        print(Fore.GREEN + f"Nome do produto foi modificado para {novo_nome} com sucesso!")

    elif opcao == 2:
        while True:
            try:
                novo_preco = float(input("Digite o novo preço do produto: "))
                break

            except ValueError:
                print(Fore.RED + "\nValor inválido! Tente novamente.")

        produto_modificado['preco'] = novo_preco
        print(Fore.GREEN + f"Preço do produto foi modificado para R$ {novo_preco:.2f} com sucesso!")

    elif opcao == 3:
        while True:
            try:
                nova_quantidade = int(input("Digite a nova quantidade do produto: "))
                break

            except ValueError:
                print(Fore.RED + "\nValor inválido! Tente novamente.")

        produto_modificado['quantidade'] = nova_quantidade
        print(Fore.GREEN + f"Quantidade do produto foi modificado para {nova_quantidade} com sucesso!")

    elif opcao == 0:
        return

def pesquisar_produtos(): #Opção 4: Buscar produto por nome 
    if not produtos:
        print("Não tem produtos ainda!") 
        return

    nome = input("Digite o nome do produto: ").lower().strip()  
    encontrado = False
    for i, produto in enumerate(produtos):
        if produto['nome'].lower() == nome:
            print(f"\n{i+1}. Nome: {produto['nome']} | Preço: R${produto['preco']:.2f} | Quantidade {produto['quantidade']}.")
            encontrado = True
        
    if encontrado == False:
        print("Produto não encontrado!")

def listar_produtos(): #Opção 5: Listar produtos.
    if not produtos:
        print("Não tem produtos ainda!") 
        return False

    else:
        print("Lista de todos os produtos:")
        for i, produto in enumerate(produtos, 1):
            print(f"\n{i}. Nome: {produto['nome']} | Preço: R${produto['preco']:.2f} | Quantidade {produto['quantidade']}.")

def calcular_todos_produtos(): #Opção 5: Calcular o valor total do estoque.
    if not produtos:
        print("Não tem produtos ainda!") 
        return

    total = 0

    for produto in produtos:
        total += produto['preco'] * produto['quantidade']

    print(f"Valor total dos produtos é R$ {total:.2f}.")

while True:
    print()
    print("1. Adicionar um produto")
    print("2. Remover um produto")
    print("3. Atualizar preço ou quantidade")
    print("4. Buscar produto por nome")
    print("5. Listar todos os produtos")
    print("6. Calcular o valor total do estoque")
    print("0. Sair do sistema")
    
    while True:
        try:
            escolha = int(input("\nEscolha uma opção: "))
            if escolha in [1, 2, 3, 4, 5, 6, 0]:
                break
            else:
                print(Fore.RED + "\nValor inválido! Tente novamente.")

        except ValueError:
            print(Fore.RED + "\nValor inválido! Tente novamente.")
        
    print()

    if escolha == 1:
        while True:
            try:
                nome = input(F"Digite o {Fore.YELLOW}nome{Fore.WHITE} produto que você quer adicionar: ")
                preco = float(input(F"Digite o {Fore.YELLOW}preço{Fore.WHITE} produto que você quer adicionar: "))
                quantidade = int(input(F"Digite o {Fore.YELLOW}quantidade{Fore.WHITE} produto que você quer adicionar: "))

            except ValueError:
                print(Fore.RED + "\nValor inválido! Tente novamente.\n")
                continue
            break
        adicionar_produtos(nome, preco, quantidade)

    elif escolha == 2:
        remover_produtos()

    elif escolha == 3:
        modificar_produto()

    elif escolha == 4:
        pesquisar_produtos()

    elif escolha == 5:
        listar_produtos()

    elif escolha == 6:
        calcular_todos_produtos()

    elif escolha == 0:
        print("Você saiu do programa")
        break