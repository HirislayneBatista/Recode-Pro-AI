class sistemaCaixaVenda:
    def __init__(self):
        self.saldo = 1300
        self.ingressoNormal = 50
        self.ingressoVip = 100 # ou com uso de dic: self.precos = {"normal": 50, "vip": 100}
        self.total = 0  # inicializacao do total arrecado com vendas
        
    def vender(self, tipoIngresso, quantidade):
        # Validações
        if tipoIngresso not in ["normal", "vip"]:
            print("\nTipo de ingresso inválido!")
            return False
        
        if quantidade <= 0:
            print("\nQuantidade inválida!")
            return False
        
        # Calcula preco total dos ingressos pelo tipo 
        preco_ingresso = self.ingressoNormal if tipoIngresso == "normal" else self.ingressoVip # com uso de dic: preco_ingresso = self.precos[tipoIngresso]  # Obtém o preço do ingresso
        valor_total = preco_ingresso * quantidade
            
        # Verificacao de saldo suficiente e realização da venda
        if (self.saldo < valor_total):
            print('\nSaldo insuficiente para essa compra!')
            return False
        
        self.saldo -= valor_total
        self.total += valor_total # atualiza total de vendas
        print(f"\nCompra realizada com sucesso! {quantidade} ingresso(s) '{tipoIngresso}' no valor de R$ {preco_ingresso} vendidos por R$ {valor_total}.")
        return True
        
    def exibirTotalVendas(self):
        return self.total  # total arrecadado

# Criar um objeto caixa
ingresso = sistemaCaixaVenda() 

# Realizar uma venda
ingresso.vender ('normal', 2) 

# Exibir total de vendas
print(f"\nTotal das vendas: R$ {ingresso.exibirTotalVendas()}")