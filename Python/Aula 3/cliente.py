def cadastrar_cliente():
    print("\nCADASTRO DE CLIENTE:")
    nome = input("\nNome do cliente: ")
    telefone = input("\nTelefone: ")
    pet = input("\nNome do pet: ")
    
    # salva no arquivo
    with open("cliente.txt", "a") as arquivo:
        arquivo.write(f"{nome},{telefone},{pet}\n")
    
    # clientes.append({"nome": nome, "telefone": telefone, "pet": pet})
    
    print(f"\n Cliente {nome} cadastrado com sucesso!")

def listar_clientes():
    print("\nLISTA DE CLIENTES:")
    # for cliente in clientes:
    #     print(f" Nome: {cliente['nome']} | Telefone: {cliente['telefone']} | Pet: {cliente['pet']}")
    
    with open("cliente.txt", "r") as arquivo:
        clientes = arquivo.readlines()
        for cliente in clientes:
            nome, telefone, pet = cliente.strip().split(",")
            print(f"\nNome Cliente: {nome}, Telefone: {telefone}, Nome do Pet: {pet}")

# listar_clientes()
