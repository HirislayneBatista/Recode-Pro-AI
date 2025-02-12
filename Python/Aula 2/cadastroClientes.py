clientes = []

def cadastro():
    nomeCliente = input("\nSeu Nome: ")
    nomePet = (input("Nome do seu Pet: "))
    telefone = input("Telefone: ")

    cadastro = {
        'NomeCliente': nomeCliente,
        'NomePet': nomePet,
        'Telefone': telefone
    }

    clientes.append(cadastro)

    print(f"\nCliente {nomeCliente} cadastrado com sucesso!")
    
    return clientes