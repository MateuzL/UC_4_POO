class Paciente:
    def __init__(self, codigo, nome, cpf, idade):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.ativo = True
    
    def exibir_dados(self):
        print("\n--- DADOS DO PACIENTE ---")
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Idade: {self.idade}")
        print(f"Situação: {'Ativo' if self.ativo else 'Inativo'}")
    
    def desativar(self):
        if not self.ativo:
            print("O paciente está inativo")
        else:
            self.ativo = False
            print(f"Paciente {self.nome} desativado com sucesso.")
    
    def ativo(self):
        if self.ativo:
            print("O paciente já está ativo.")
        else:
            self.ativo = True
            print(f"Paciente {self.nome} ativado com sucesso.")
