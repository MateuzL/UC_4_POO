class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_dados(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Quantidade em estoque: {self.quantidade}")

    def calcular_total_estoque(self):
        total = self.preco * self.quantidade
        print(f"Valor total em estoque: R$ {total:.2f}")

p1 = Produto("Mouse", 50.00, 10)
p2 = Produto("Teclado", 120.00, 5)

p1.mostrar_dados()
p1.calcular_total_estoque()
print()

p2.mostrar_dados()
p2.calcular_total_estoque()
