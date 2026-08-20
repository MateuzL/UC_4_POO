class Pedido:
    def __init__(self, codigo, cliente, produto, status):
        self.codigo = codigo
        self.cliente = cliente
        self.produto = produto
        self.status = "Pendente"

    def validar_pedido(self):

        if self.produto <= 0:
            print("Erro: A quantidade de produtos deve ser maior que 0.")
            return False

        return True
    