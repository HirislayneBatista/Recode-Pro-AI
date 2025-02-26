class Caixa:
    def __init__(self):
        self.saldo = 1000
    def sacar(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print(f'Saque de R$ {valor} realizado com sucesso!')
        else:
            print('Saldo insuficiente!')
            
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R$ {valor} realizado com sucesso!")
        
    def exibir_saldo(self):
        return self.saldo

# Criar um objeto caixa
caixa = Caixa() 

# Realizar deposito
caixa.depositar (500) 
print("Saldo atual:", caixa.exibir_saldo())