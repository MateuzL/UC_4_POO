class Cliente:
    def __init__(self, codigo, nome, telefone):
        self.codigo = codigo
        self.__nome = ""
        self.__telefone = ""

        self.set_nome(nome)
        self.set_telefone(telefone)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        nome = nome.strip()
        if len(nome) <= 0:
            print("Erro: o nome não deve ficar vazio.")
            return False
        if len(nome) < 3:
            print("Erro: O nome não deve ter menos que 3 caracteres.")
        
        self.__nome = nome
        return True

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        if len(telefone) <= 0:
            print("Erro: O Telefone não pode ficar vazio.")
            return False
        self.__telefone = telefone
        return True


    def exibir_dados(self):
        print("--- DADOS CLIENTE ---")
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.__nome}")
        print(f"Telefone: {self.__telefone}")
