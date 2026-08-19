from pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, curso):
        super().__init__(nome, cpf)
        self.__matricula = matricula
        self.__curso = curso

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_curso(self):
        return self.__curso

    def set_curso(self, curso):
        self.__curso = curso

    def exibir_dados(self):
        print("=== DADOS DO ALUNO ===")
        print(f"Nome: {self.get_nome()}")
        print(f"CPF: {self.get_cpf()}")
        print(f"Matrícula: {self.__matricula}")
        print(f"Curso: {self.__curso}")
