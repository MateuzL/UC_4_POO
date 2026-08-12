class Cliente:
    """
    Representa um cliente da locadora.

    Conceitos trabalhados:
    - Classe e objeto
    - Construtor
    - Encapsulamento
    - Getters e setters
    - Validação de dados
    """

    def __init__(self, codigo, nome, cpf):
        # O código é público porque será usado como identificador do cliente.
        self.codigo = codigo

        # Nome e CPF são privados para evitar alterações diretas indevidas.
        self.__nome = ""
        self.__cpf = ""

        # Usamos os setters no construtor para validar os dados recebidos.
        self.set_nome(nome)
        self.set_cpf(cpf)

    def get_nome(self):
        """Retorna o nome do cliente."""
        return self.__nome

    def set_nome(self, nome):
        """
        Altera o nome do cliente.
        Regra: o nome deve possuir pelo menos 3 caracteres.
        """
        nome = nome.strip()

        if len(nome) < 3:
            print("Erro: o nome deve possuir pelo menos três caracteres.")
            return False

        self.__nome = nome
        return True

    def get_cpf(self):
        """Retorna o CPF do cliente."""
        return self.__cpf

    def set_cpf(self, cpf):
        """
        Altera o CPF do cliente.
        Para fins didáticos, valida apenas se há 11 dígitos numéricos.
        """
        cpf_limpo = cpf.replace(".", "").replace("-", "").strip()

        if not cpf_limpo.isdigit() or len(cpf_limpo) != 11:
            print("Erro: o CPF deve possuir exatamente 11 números.")
            return False

        self.__cpf = cpf_limpo
        return True

    def exibir_dados(self):
        """Exibe os dados do cliente."""
        print("\n--- DADOS DO CLIENTE ---")
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.__nome}")
        print(f"CPF: {self.__cpf}")