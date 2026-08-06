class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        