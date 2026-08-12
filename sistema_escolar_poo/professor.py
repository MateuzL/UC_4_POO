from pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.__disciplina = disciplina
        self.__salario = salario

    # Getter e Setter da disciplina
    def get_disciplina(self):
        return self.__disciplina

    def set_disciplina(self, disciplina):
        if not disciplina.strip():
            raise ValueError("A disciplina não pode ficar vazia.")
        self.__disciplina = disciplina

    # Getter e Setter do salário
    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        self.__salario = salario

    # Método 1
    def ministrar_aula(self):
        return f"{self.get_nome()} está ministrando a disciplina de {self.__disciplina}."

    # Método 2
    def aumentar_salario(self, percentual):
        if percentual <= 0:
            raise ValueError("O percentual deve ser maior que zero.")
        self.__salario += self.__salario * (percentual / 100)

    # Método 3
    def exibir_informacoes(self):
        return (
            f"Professor: {self.get_nome()} | "
            f"Disciplina: {self.__disciplina} | "
            f"Salário: R$ {self.__salario:.2f}"
        )

    def exibir_tipo(self):
        return "Professor"
