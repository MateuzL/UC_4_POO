from pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, cpf, registro, departamento):
        super().__init__(nome, cpf)
        self.__registro = registro
        self.__departamento = departamento

    def get_registro(self):
        return self.__registro

    def set_registro(self, registro):
        self.__registro = registro

    def get_departamento(self):
        return self.__departamento

    def set_departamento(self, departamento):
        self.__departamento = departamento

    def exibir_dados(self):
        print("=== DADOS DO PROFESSOR ===")
        print(f"Nome: {self.get_nome()}")
        print(f"CPF: {self.get_cpf()}")
        print(f"Registro: {self.__registro}")
        print(f"Departamento: {self.__departamento}")
