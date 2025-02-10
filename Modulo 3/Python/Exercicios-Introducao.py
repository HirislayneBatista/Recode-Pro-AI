# Exercicio 1
print("-- Qual dos 2 numero eh o maior?\n")
numero1 = int(input("Informe o primeiro numero: "))
numero2 = int(input("Informe o segundo numero: "))

if numero1 > numero2:
    print("O maior numero é o: ", numero1)
else:
    print("O maior numero é o: ", numero2)
    
# Exercicio 2
print("\n\n -- Voce pode dirigir?\n")
idade = int(input("Informe a sua idade: "))   
if idade >= 18:
    print("Você é maior de idade e pode dirigir!") 
else:
    print("Infelizmente voce ainda não pode dirigir por ser menor de idade.")
    
# Exercicio 3
print("\n\n-- O numero é par ou Impar?\n")
numeroParImpar = int(input("Informe o seu numero: "))
if numeroParImpar % 2 == 0:
    print("O numero é par.\n")
else:
    print("O numero é impar.\n")