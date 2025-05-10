def cadastrar_cliente():
    print("\nCADASTRO DE CLIENTE:")
    nome = input("\nNome do cliente: ")
    telefone = input("Telefone: ")
    pet = input("Nome do pet: ")
    
    # Salva no arquivo
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(f"{nome}, {telefone}, {pet}\n")
    
    print(f"\n Cliente {nome} cadastrado com sucesso!")

def listar_clientes():
    print("\nLISTA DE CLIENTES:")
    
    # Ler o arquivo
    with open("clientes.txt", "r") as arquivo:
        clientes = arquivo.readlines()
        for cliente in clientes:
            nome, telefone, pet = cliente.strip().split(", ")
            print(f"\nNome Cliente: {nome} | Telefone: {telefone} | Nome do Pet: {pet}")

# cadastrar_cliente()
# listar_clientes()