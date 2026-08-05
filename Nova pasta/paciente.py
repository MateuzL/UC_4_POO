class Paciente:
    def __init__(self, codigo, nome, cpf, idade):
        self.codigo = codigo
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome.strip() == "":
            print("Nome é inválido.")
        else:
            self.__nome = nome
            print("Nome atualizado.")

    def get_cpf(self):
         return self.__cpf

    def set_cpf(self, cpf):
         cpf = cpf.replace(".", "").replace(".", "")

         if len(cpf) == 11 and cpf.isdigit():
              self.__cpf = cpf
              print("CPF Atualizado.")
         else:
              print("CPF Inválido.")

    def get_idade(self):
         return self.__idade

    def set_idade(self, idade):
         if idade >= 0:
              self.__idade = idade
         else:
              print("Idade Inválida")

    def exibir_dados(self):
            print(f"\n--- Paciente ---")
            print(f"Código: {self.codigo}")
            print(f"Nome: {self.get_nome()}")
            print(f"CPF: {self.get_cpf()}")
            print(f"Idade: {self.get_idade()}")