from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, cpf, registro, departamento):
        super().__init__(nome, cpf)

        self.__registro = ""
        self.__departamento = ""

        self.set_registro(registro)
        self.set_departamento(departamento)

    def get_registro(self):
        return self.__registro

    def set_registro(self, registro):
        registro = registro.strip()

        if len(registro) < 3:
            print("Erro: O registro deve conter pelo menos três caracteres.")
            return False
            
        self.__registro = registro
        return True


    def get_departamento(self):
        return self.__departamento

    def set_departamento(self, departamento):
        departamento = departamento.strip()

        if len(departamento) < 3:
            print("Erro: O departamento deve conter pelo menos três caracteres.")
            return False

        self.__departamento = departamento
        return True

    def exibir_dados(self):
        print("--- DADOS PROFESSOR ---")
        super().exibir_dados()
        print(f"Registro: {self.get_registro()}")
        print(f"Departamento: {self.get_departamento()}")

        
