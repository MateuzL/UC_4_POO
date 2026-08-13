class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = ""
        self.__cpf = ""

        self.set_nome(nome)
        self.set_cpf(cpf)

    def get_nome(self):
            return self.__nome

    def set_nome(self, nome):

        nome = nome.strip()
        if len(nome) < 3:
            print("Erro: o nome deve possuir pelo menos três caracteres.")
            return False
        self.__nome = nome
        return True

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):

        cpf_limpo = cpf.replace(".","").replace(".", "").strip()

        if not cpf_limpo.isdigit() or len(cpf_limpo) != 11:
            print("Erro: O CPF deve conter exatamente 11 dígitos.")
            return False
        self.__cpf = cpf_limpo
        return True

    def exibir_dados(self):
        print(f"Nome: {self.get_nome()}")
        print(f"CPF: {self.get_cpf()}")

        

