class Sala:

    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade
        self.disponivel = True

    def cadastrar(self):
        print(f"Sala {self.numero} cadastrada.")

    def alterar(self, capacidade):
        self.capacidade = capacidade
        print(f"Sala {self.numero} alterada.")

    def excluir(self):
        print(f"Sala {self.numero} excluída.")

    def consultarDisponibilidade(self):
        return self.disponivel