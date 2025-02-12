# Lista para armazenar os pets cadastrados - inicialmente vazia
pets = []

# Funcao para cadastrar um pet 
def cadastrarPet():
    nome = input("\nNome do Pet: ")
    especie = input("Espécie do Pet: ")
    idade = int(input("Idade do Pet (em anos): "))
    saude = input("O pet está saudavel (s/n): ")

    simNao = "Sim" if (saude == "s") else "Não"
    
    novoPet = {
        'Nome': nome,
        'Espécie': especie,
        'Idade': idade,
        'Saude': simNao
    }
    
    pets.append(novoPet)
    
    print(f"\nPet {nome} cadastrado com sucesso!")

# Funcao para listar os pets cadastrados
def listarPet():
    if len(pets) == 0:
        print("\nNenhum pet cadastrado.")
    else:
        print("\nPets Cadastrados:")
        for i in pets:
            print("-" * 30)
            print(f"\nNome: {i['Nome']} | Espécie: {i['Espécie']} | Idade: {i['Idade']} | Saudável: {i['Saude']}\n")
            print("-" * 30)

# Menu principal
while True:
    print("\n -- SEU PETSHOP: MENU PRINCIPAL --\n")
    print("1 - Cadastrar Pet")
    print("2 - Listar Pets")
    print("3 - Sair\n")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        cadastrarPet()
        
    elif opcao == 2:
        listarPet()
        
    elif opcao == 3:
        print("\nSistema encerrado.\n")
        break

    else:
        print("\nOpção inválida. Tente novamente.\n")