lista = []

while True:
    try: # Inicia um loop infinito
        print("Menu:")
        opcao = input("Selecione uma opção: \n{i}nserir {a}pagar {l}istar {s}air: ").lower() # Converte a opção para minúscula
        if opcao == 'i':
            item = input("Digite o item a ser inserido: ").strip() # Remove espaços em branco no início e no fim
            if item == '' and not item.isalpha: # Verifica se o item é vazio ou não contém letras
                print("Item inválido.")
                continue # Continua o loop se o item for inválido
            lista.append(item) # Adiciona o item à lista
            if lista: # Verifica se a lista não está vazia
                print("Lista de compras:")
                for indice, item in enumerate(lista): # Enumerate retorna o índice e o valor do item
                    print(f"{indice} {item}")
            else:
                print("A lista está vazia.")
        elif opcao == 'a':
            indice = int(input("Digite o índice do item a ser apagado: "))
            if indice >= 0 and indice < len(lista): # Verifica se o índice é válido
                lista.pop(indice)
                print("Item apagado com sucesso.")
                if lista: # Verifica se a lista não está vazia
                    print("Lista de compras atualizada:")
                    for indice, item in enumerate(lista):
                        print(f"{indice} {item}")
                else:
                    print("A lista está vazia.")
            else:
                print("Não foi possivel apagar esse indice.")
        elif opcao == 'l':
            if lista:
                print("Lista de compras:")
                for indice, item in enumerate(lista):
                    print(f"{indice}: {item}")
            else:
                print("A lista está vazia.")
        elif opcao == 's':
            print("Saindo do programa.")
            break # Encerra o loop
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError: # Captura erro de conversão de tipo
        print("Valor inválido. Tente novamente.")

