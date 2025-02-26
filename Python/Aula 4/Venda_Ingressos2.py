class sistemaCaixaVenda:
    def __init__(self):
        self.saldo = 1300
        self.ingressoNormal = 50
        self.ingressoVip = 100
        self.total = 0  # total arrecado com vendas
        
    def vender(self, tipoIngresso, quantidade):
        if (tipoIngresso == 'normal'):
            compraIngresso = self.ingressoNormal * quantidade
        else:
            compraIngresso = self.ingressoVip * quantidade
        
        if (self.saldo >= compraIngresso):
            self.saldo -= compraIngresso
            self.total += compraIngresso # atualiza total de vendas
            print(f'Saque do ingresso no valor de R$ {compraIngresso} realizado com sucesso!')
        else:
            print('Saldo insuficiente!')
            
            
        # Realiza a venda
        self.saldo -= compraIngresso
        self.total += compraIngresso
        print(f"Compra realizada com sucesso! {quantidade} ingresso(s) '{tipoIngresso}' vendidos por R$ {compraIngresso}.")
        return True
        
    def exibirTotalVendas(self):
        return self.total  # total arrecadado

# Criar um objeto caixa
ingresso = sistemaCaixaVenda() 

# Realizar uma venda
tipoIngresso = 'vip'
quantidade = 10
ingresso.vender (tipoIngresso, quantidade) 

# Exibir total de vendas
print(f"Total arrecadado: R$ {ingresso.exibirTotalVendas()}")