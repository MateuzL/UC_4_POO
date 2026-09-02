class Usuario:

    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login_usuario = login
        self.senha = senha
        self.logado = False

    def login(self, login, senha):
        if login == self.login_usuario and senha == self.senha:
            self.logado = True
            print("Login realizado com sucesso!")
        else:
            print("Login ou senha incorretos.")

    def logout(self):
        self.logado = False
        print("Logout realizado com sucesso.")

    def cadastrar(self):
        print(f"Usuário {self.nome} cadastrado com sucesso!")