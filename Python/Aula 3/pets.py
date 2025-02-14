def cadastrar_pet():
    print("\nCADASTRO DE PETS:\n")
    try:
        nome = input("Nome do pet: ")
        especie = input("Espécie (Cachorro, Gato, etc.): ")
        idade = int(input("Idade do pet (em anos): "))
        status = input("O pet está saudável? (s/n): ").lower() == "s"

        categoria = "Filhote" if idade < 2 else "Adulto" if idade < 8 else "Senior"
        saudavel = "Sim" if status == True else "Nao"
        
        # Salva no arquivo
        with open("pets.txt", "a") as arquivo:
            arquivo.write(f"{nome}, {especie}, {idade}, {categoria}, {saudavel}\n")
        
        print(f"\nPet {nome} cadastrado com sucesso!")

    except ValueError:
        print("Erro: Idade deve ser um número válido!")

def listar_pets():
    print("\nLISTA DE PETS CADASTRADOS:\n")
    
    # Ler o arquivo
    with open("pets.txt", "r") as arquivo:
        pets = arquivo.readlines()
        for pet in pets:
            nome, especie, idade, categoria, saudavel = pet.strip().split(", ")
            print(f"Nome do pet: {nome} | Espécie: {especie} | Idade: {idade} anos | Categoria: {categoria} | Saudável: {saudavel}")

cadastrar_pet()
listar_pets()