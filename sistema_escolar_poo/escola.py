from aluno import Aluno
from professor import Professor


class Escola:
    def __init__(self, nome):
        self.__nome = nome
        self.__alunos = []
        self.__professores = []

    # Getter e Setter do nome
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if not nome.strip():
            raise ValueError("O nome da escola não pode ficar vazio.")
        self.__nome = nome

    # Getter dos alunos
    def get_alunos(self):
        return self.__alunos

    # Getter dos professores
    def get_professores(self):
        return self.__professores

    # Método 1
    def adicionar_aluno(self, aluno):
        if not isinstance(aluno, Aluno):
            raise TypeError("O objeto precisa ser um Aluno.")
        self.__alunos.append(aluno)

    # Método 2
    def adicionar_professor(self, professor):
        if not isinstance(professor, Professor):
            raise TypeError("O objeto precisa ser um Professor.")
        self.__professores.append(professor)

    # Método 3
    def listar_pessoas(self):
        pessoas = []
        for aluno in self.__alunos:
            pessoas.append(aluno.apresentar())

        for professor in self.__professores:
            pessoas.append(professor.apresentar())

        return pessoas
