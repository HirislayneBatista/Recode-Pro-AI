import pets
import cliente
import servicos

while True:
    print("\nPETSHOP MANAGER - MENU PRINCIPAL")
    print("1 - Cadastrar Pet")
    print("2 - Listar Pets")
    print("3 - Cadastrar Cliente")
    print("4 - Listar Clientes")
    print("5 - Agendar Servico")
    print("6 - Listar Servicos")
    print("7 - Sair")

    opcao = input("\nEscolha uma opcao: ")

    if opcao == "1":
        pets.cadastrar_pet()
    elif opcao == "2":
        pets.listar_pets()
    elif opcao == "3":
        cliente.cadastrar_cliente()
    elif opcao == "4":
        cliente.listar_clientes()
    elif opcao == "5":
        servicos.agendar_servico()
    elif opcao == "6":
        servicos.listar_servicos()
    elif opcao == "7":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
