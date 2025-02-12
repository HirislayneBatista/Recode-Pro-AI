def listagem(clientes):
    if len(clientes) == 0:
        print("\nNenhum cliente cadastrado.")
    else:
        print("\nClientes Cadastrados:")
        print("-" * 30)
        for i in clientes:
            print(f"\nCliente: {i['NomeCliente']} | Pet: {i['NomePet']} | Telefone: {i['Telefone']}\n")