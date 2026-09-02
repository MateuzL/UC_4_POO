class Turma:

    def __init__(self, nome, curso, quantidade_alunos):
        self.nome = nome
        self.curso = curso
        self.quantidade_alunos = quantidade_alunos

    def cadastrar(self):
        print(f"Turma {self.nome} cadastrada com sucesso!")

    def alterar(self, curso, quantidade_alunos):
        self.curso = curso
        self.quantidade_alunos = quantidade_alunos
        print(f"Turma {self.nome} alterada com sucesso!")

    def excluir(self):
        print(f"Turma {self.nome} excluída com sucesso!")

    def consultar(self):
        print("\n--- TURMA ---")
        print(f"Nome: {self.nome}")
        print(f"Curso: {self.curso}")
        print(f"Quantidade de alunos: {self.quantidade_alunos}")