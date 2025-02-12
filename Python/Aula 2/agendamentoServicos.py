def servico(clientes):
    nome_cliente = input("Informe o nome do cliente: ").strip()
    servico = None
    opcao = 0
    
    # Verifica primeiro se o nome do cliente existe, se não existir solicita os dados do cliente antes do tipo de servico
    cliente_encontrado = False
    for cliente in clientes:
        if not cliente_encontrado:
            nome_cliente = input("Informe o nome do cliente: ")
            nome_pet = input("Informe o nome do pet: ").strip()
            telefone = input("Telefone: ").strip()
            continue
        
        
        if cliente["NomeCliente"].lower() == nome_cliente.lower(): continue
        
        while opcao != 4:
            print("\nServicos disponiveis:\n1 - Banho\n 2 - Tosa\n 3 - Consulta\n4 - Cancelar\n")
            opcao = int(input("Escolha uma opcao: "))

            if opcao == 1:
                servico = "Banho"
                
            elif opcao == 2:
                servico = "Tosa"
                
            elif opcao == 3:
                servico = "Consulta"
            
            elif opcao == 4:
                print("Operacao cancelada\n")
                return

            else:
                print("Opcao invalida. Tente novamente!\n")
                continue
            
            print(f"{servico} agendado para {nome_cliente}!\n")
            break 
            
    cliente["Serviços"].append(servico)
    cliente_encontrado = True
            
            # Verificacao pra ver se o cliente ja está na lista 
            # cliente_encontrado = False
            # for cliente in clientes:
            #     if cliente["NomeCliente"].lower() == nome_cliente.lower():
            #         cliente["Serviços"].append(servico)
            #         cliente_encontrado = True
            #         break
                
            # if not cliente_encontrado:
            #     nome_pet = input("Informe o nome do seu pet: ").strip()
            #     telefone = input("Informe seu telefone: ").strip()
                
            #     clientes.append(
            #         {
            #             "Nome": nome_cliente, 
            #             "NomePet": nome_pet,
            #             "Telefone": telefone,
            #             "Serviços": [servico]
            #         }
            #     )
        
        # servicoAgendado = {
            #     'Serviço': servico
            # }
            # clientes.append(servicoAgendado)