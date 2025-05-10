def agendar_servico():
    print("\nAGENDAMENTO DE SERVICOS:\n")
    dono = input("Nome do cliente: ")
    pet = input("Nome do pet: ")
    servico = input("Serviço (Banho, Tosa, Consulta): ")
    
    # Salva no arquivo
    with open("agendamentos.txt", "a") as arquivo:
        arquivo.write(f"{dono}, {pet}, {servico}\n")
    
    print(f"\nServiço '{servico}' agendado para {pet}!")

def listar_servicos():
    print("\nLISTA DE SERVIÇOS AGENDADOS:")
    
    with open("agendamentos.txt", "r") as arquivo:
        agendamentos = arquivo.readlines()
        for agenda in agendamentos:
            dono, pet, servico = agenda.strip().split(", ")
            print(f"\n{dono} agendou {servico} para {pet}.")

# agendar_servico()
# listar_servicos()