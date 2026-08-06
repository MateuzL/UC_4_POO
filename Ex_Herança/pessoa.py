class Pessoa:
    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco

    def apresentar(self):
        print("\n --- PESSOA ---")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")