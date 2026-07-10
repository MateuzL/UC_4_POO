class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}.")
        print(f"Tenho {self.idade} anos.")
        print(f"A minha matricula é {self.matricula}.")

info1 = Aluno("João", 20, 1928475)
info2 = Aluno("Maria", 19, 112233)

info1.apresentar()
print()
info2.apresentar()
