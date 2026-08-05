class Funcionario:
    def __init__(self, matricula, nome, cargo, salario):
        self.matricula = matricula
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def set_salario(self, novo_salario):
        if novo_salario <= 1621:
            print("Erro! Salário abaixo do mínimo.")
        elif novo_salario > 10000:
            print("Erro! Salário imcompatível")
        else:
            self.__salario = novo_salario
            print("Salário Atualizado.")

    def exibir_dados(self):
        print("--- FUNCIONÁRIO ---")
        print(f"Matrícula: {self.matricula}")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: {self.__salario}")
         