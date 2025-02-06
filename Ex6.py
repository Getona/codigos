class Produto:
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade

    def valor_total_estoque(self):
        return self.preço * self.quantidade
    
    def esta_disponivel(self):
        return self.quantidade > 0

#Exemplo de uso:    
produto = Produto("Celular, 1500.00, 10")

print(f"Produto: {produto.nome}")
print(f"Preço unitário: R${produto.preço}")
print(f"Quantidade em estoque: {produto.quantidade}")
print(f"Valor total em estoque: R${produto.valor_total_estoque()}")
print(f"Produto disponivel: {'Sim' if produto.esta_disponivel() else 'Não'}")