class Pedido:

    def __init__(self, codigo, cliente):
        self.codigo = codigo
        self.cliente = cliente
        self.produtos = []
        self.status = "Aberto"

    def adicionar_produto(self, produto):

        if self.status == "Finalizado":
            print("Não é possível adicionar produtos a um pedido finalizado.")
            return False

        self.produtos.append(produto)
        return True

    def finalizar(self):

        if len(self.produtos) == 0:
            print("Não é possível finalizar um pedido sem produtos.")
            return False

        self.status = "Finalizado"
        return True

    def calcular_total(self):

        total = 0

        for produto in self.produtos:
            total += produto.get_preco()

        return total

    def exibir_resumo(self):

        
        print("\n ----- RESUMO DO PEDIDO -----")

        print(f"Pedido: {self.codigo}")
        print(f"Cliente: {self.cliente.get_nome()}")
        print(f"Telefone: {self.cliente.get_telefone()}")
        print(f"Status: {self.status}")

        print("\nProdutos:")

        for produto in self.produtos:
            print(f"\n - {produto.nome}")
            print(f"\nR$ {produto.get_preco():.2f}")

        print(f"\nTOTAL: R$ {self.calcular_total():.2f}")
        print("==============================")

