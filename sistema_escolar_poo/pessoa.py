class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    # Getter e Setter do nome
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if not nome.strip():
            raise ValueError("O nome não pode ficar vazio.")
        self.__nome = nome

    # Getter e Setter da idade
    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        self.__idade = idade

    # Método 1
    def apresentar(self):
        return f"Nome: {self.__nome} | Idade: {self.__idade}"

    # Método 2
    def fazer_aniversario(self):
        self.__idade += 1
        return f"{self.__nome} agora tem {self.__idade} anos."

    # Método 3
    def exibir_tipo(self):
        return "Pessoa"
