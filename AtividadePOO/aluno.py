from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, curso):
        super().__init__(nome, cpf)
        self.__matricula = ""
        self.__curso = ""

        self.set_matricula(matricula)
        self.set_curso(curso)


    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        matricula = matricula.strip()
            
        if len(matricula) < 3:
            print("Erro: o nome deve possuir pelo menos três caracteres.")
            return False
            
        self.__matricula = matricula
        return True

    def get_curso(self):
        return self.__curso

    def set_curso(self, curso):
        curso = curso.strip()

        if len(curso) < 3:
            print("Erro: O curso deve possuir pelo menos três caracteres.")
            return False
        self.__curso = curso
        return True

    def exibir_dados(self):
        print("--- DADOS ALUNO ---")
        super().exibir_dados()
        print(f"Matricula: {self.get_matricula()}")
        print(f"Curso: {self.get_curso()}")

        