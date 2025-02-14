clientes = []

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    pet = input("Nome do pet: ")
    clientes.append({"nome": nome, "telefone": telefone, "pet": pet})
    print(f"\n✅ Cliente {nome} cadastrado com sucesso!")

def listar_clientes():
    print("\n📋 LISTA DE CLIENTES:")
    for cliente in clientes:
        print(f"👤 Nome: {cliente['nome']} | Telefone: {cliente['telefone']} | Pet: {cliente['pet']}")
