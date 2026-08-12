from pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.__matricula = matricula
        self.__notas = []

    # Getter e Setter da matrícula
    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        if not matricula.strip():
            raise ValueError("A matrícula não pode ficar vazia.")
        self.__matricula = matricula

    # Getter e Setter das notas
    def get_notas(self):
        return self.__notas

    def set_notas(self, notas):
        for nota in notas:
            if nota < 0 or nota > 10:
                raise ValueError("As notas devem estar entre 0 e 10.")
        self.__notas = notas

    # Método 1
    def adicionar_nota(self, nota):
        # Regra de negócio 1: nota deve estar entre 0 e 10.
        if nota < 0 or nota > 10:
            raise ValueError("A nota deve estar entre 0 e 10.")
        self.__notas.append(nota)

    # Método 2
    def calcular_media(self):
        if not self.__notas:
            return 0
        return sum(self.__notas) / len(self.__notas)

    # Método 3
    def verificar_aprovacao(self):
        # Regra de negócio 2: aluno precisa de média >= 6 para aprovação.
        media = self.calcular_media()
        if media >= 6:
            return "Aprovado"
        return "Reprovado"

    def exibir_tipo(self):
        return "Aluno"
