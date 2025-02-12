# Uso de modulos
import cadastroClientes
import listagemClientes
import agendamentoServicos

clientes = []
servicos = []

# Menu principal
while (True):
    print("\n -- Cadastro de Clientes e Serviços --\n")
    print("1 - Cadastro Cliente")
    print("2 - Listagem de Clientes Cadastrados")
    print("3 - Agendamento de Serviços")
    print("4 - Listagem de Serviços Agendados")
    print("5 - Cancelamento de Agendamentos")
    print("6 - Sair\n")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        clientes = cadastroClientes.cadastro()
        
    elif opcao == 2:
        if clientes:
            listagemClientes.listagem(clientes)
        else:
            print("\nNenhum cliente cadastrado ainda.\n")

    elif opcao == 3:
        agendamentoServicos.servico(clientes)
   
    # elif opcao == 6:
    #     print("\nSistema encerrado.\n")
    #     break

    else:
        print("\nOpção inválida. Tente novamente.\n")