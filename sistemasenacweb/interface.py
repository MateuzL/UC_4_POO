import tkinter as tk
from tkinter import messagebox
import os

from coordenador import Coordenador
from professor import Professor
from sala import Sala
from turma import Turma
from reserva import Reserva


class SistemaInterface:

    # ==================================================
    # CORES DO SISTEMA
    # ==================================================

    AZUL = "#005CA9"
    AZUL_ESCURO = "#003B70"
    AZUL_CLARO = "#EAF4FC"

    BRANCO = "#FFFFFF"
    CINZA = "#F4F6F8"
    CINZA_TEXTO = "#5F6B76"
    CINZA_BORDA = "#D9E0E6"

    VERDE = "#198754"
    VERMELHO = "#DC3545"
    LARANJA = "#F59E0B"

    # ==================================================
    # INICIALIZAÇÃO
    # ==================================================

    def __init__(
        self,
        root,
        usuarios,
        salas,
        turmas,
        reservas
    ):

        self.root = root

        self.usuarios = usuarios
        self.salas = salas
        self.turmas = turmas
        self.reservas = reservas

        self.usuario_logado = None

        self.arquivo_dados = "dados.txt"

        self.root.title(
            "Sistema da Instituição de Ensino"
        )

        self.root.geometry(
            "900x600"
        )

        self.root.resizable(
            False,
            False
        )

        self.root.configure(
            bg=self.CINZA
        )

        self.carregar_dados()

        self.tela_login()

    # ==================================================
    # LIMPAR TELA
    # ==================================================

    def limpar_tela(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    # ==================================================
    # BOTÃO PADRÃO
    # ==================================================

    def criar_botao(
        self,
        parent,
        texto,
        comando,
        largura=20,
        cor=None
    ):

        if cor is None:
            cor = self.AZUL

        botao = tk.Button(
            parent,
            text=texto,
            command=comando,
            width=largura,
            height=2,
            bg=cor,
            fg=self.BRANCO,
            activebackground=self.AZUL_ESCURO,
            activeforeground=self.BRANCO,
            relief="flat",
            bd=0,
            cursor="hand2",
            font=("Arial", 10, "bold")
        )

        return botao

    # ==================================================
    # SALVAR DADOS
    # ==================================================

    def salvar_dados(self):

        try:

            with open(
                self.arquivo_dados,
                "w",
                encoding="utf-8"
            ) as arquivo:

                arquivo.write(
                    "=== USUARIOS ===\n"
                )

                for usuario in self.usuarios:

                    if isinstance(
                        usuario,
                        Coordenador
                    ):
                        tipo = "Coordenador"
                    else:
                        tipo = "Professor"

                    arquivo.write(
                        f"{tipo}|"
                        f"{usuario.nome}|"
                        f"{usuario.login_usuario}|"
                        f"{usuario.senha}\n"
                    )

                arquivo.write(
                    "=== SALAS ===\n"
                )

                for sala in self.salas:

                    disponivel = (
                        "1"
                        if sala.disponivel
                        else "0"
                    )

                    arquivo.write(
                        f"{sala.numero}|"
                        f"{sala.capacidade}|"
                        f"{disponivel}\n"
                    )

                arquivo.write(
                    "=== TURMAS ===\n"
                )

                for turma in self.turmas:

                    arquivo.write(
                        f"{turma.nome}|"
                        f"{turma.curso}|"
                        f"{turma.quantidade_alunos}\n"
                    )

                arquivo.write(
                    "=== RESERVAS ===\n"
                )

                for reserva in self.reservas:

                    arquivo.write(
                        f"{reserva.professor.login_usuario}|"
                        f"{reserva.sala.numero}|"
                        f"{reserva.turma.nome}|"
                        f"{reserva.data}|"
                        f"{reserva.horario}|"
                        f"{reserva.status}\n"
                    )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Erro ao salvar os dados:\n{erro}"
            )

    # ==================================================
    # CARREGAR DADOS
    # ==================================================

    def carregar_dados(self):

        if not os.path.exists(
            self.arquivo_dados
        ):
            return

        try:

            with open(
                self.arquivo_dados,
                "r",
                encoding="utf-8"
            ) as arquivo:

                linhas = arquivo.readlines()

            secao = ""

            usuarios_temp = {}
            salas_temp = {}
            turmas_temp = {}

            for linha in linhas:

                linha = linha.strip()

                if not linha:
                    continue

                if linha == "=== USUARIOS ===":
                    secao = "usuarios"
                    continue

                if linha == "=== SALAS ===":
                    secao = "salas"
                    continue

                if linha == "=== TURMAS ===":
                    secao = "turmas"
                    continue

                if linha == "=== RESERVAS ===":
                    secao = "reservas"
                    continue

                dados = linha.split("|")

                # USUÁRIOS

                if secao == "usuarios":

                    tipo = dados[0]
                    nome = dados[1]
                    login = dados[2]
                    senha = dados[3]

                    if tipo == "Coordenador":

                        usuario = Coordenador(
                            nome,
                            login,
                            senha
                        )

                    else:

                        usuario = Professor(
                            nome,
                            login,
                            senha
                        )

                    self.usuarios.append(
                        usuario
                    )

                    usuarios_temp[login] = usuario

                # SALAS

                elif secao == "salas":

                    numero = dados[0]

                    capacidade = int(
                        dados[1]
                    )

                    disponivel = (
                        dados[2] == "1"
                    )

                    sala = Sala(
                        numero,
                        capacidade
                    )

                    sala.disponivel = (
                        disponivel
                    )

                    self.salas.append(
                        sala
                    )

                    salas_temp[numero] = sala

                # TURMAS

                elif secao == "turmas":

                    nome = dados[0]
                    curso = dados[1]

                    quantidade = int(
                        dados[2]
                    )

                    turma = Turma(
                        nome,
                        curso,
                        quantidade
                    )

                    self.turmas.append(
                        turma
                    )

                    turmas_temp[nome] = turma

                # RESERVAS

                elif secao == "reservas":

                    login_professor = dados[0]
                    numero_sala = dados[1]
                    nome_turma = dados[2]

                    data = dados[3]
                    horario = dados[4]
                    status = dados[5]

                    professor = (
                        usuarios_temp.get(
                            login_professor
                        )
                    )

                    sala = (
                        salas_temp.get(
                            numero_sala
                        )
                    )

                    turma = (
                        turmas_temp.get(
                            nome_turma
                        )
                    )

                    if (
                        professor
                        and sala
                        and turma
                    ):

                        reserva = Reserva(
                            professor,
                            sala,
                            turma,
                            data,
                            horario
                        )

                        reserva.status = status

                        self.reservas.append(
                            reserva
                        )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Erro ao carregar os dados:\n{erro}"
            )

    # ==================================================
    # TELA DE LOGIN
    # ==================================================

    def tela_login(self):

        self.limpar_tela()

        fundo = tk.Frame(
            self.root,
            bg=self.CINZA
        )

        fundo.pack(
            fill="both",
            expand=True
        )

        # Painel azul esquerdo

        painel_esquerdo = tk.Frame(
            fundo,
            bg=self.AZUL_ESCURO,
            width=330
        )

        painel_esquerdo.pack(
            side="left",
            fill="y"
        )

        painel_esquerdo.pack_propagate(
            False
        )

        tk.Label(
            painel_esquerdo,
            text="INSTITUIÇÃO\nDE ENSINO",
            bg=self.AZUL_ESCURO,
            fg=self.BRANCO,
            font=("Arial", 25, "bold"),
            justify="center"
        ).pack(
            pady=(130, 20)
        )

        tk.Label(
            painel_esquerdo,
            text="Sistema de Gestão Acadêmica",
            bg=self.AZUL_ESCURO,
            fg="#D9EAF7",
            font=("Arial", 11)
        ).pack()

        # Área direita

        painel_direito = tk.Frame(
            fundo,
            bg=self.BRANCO
        )

        painel_direito.pack(
            side="right",
            fill="both",
            expand=True
        )

        tk.Label(
            painel_direito,
            text="Bem-vindo!",
            bg=self.BRANCO,
            fg=self.AZUL_ESCURO,
            font=("Arial", 25, "bold")
        ).pack(
            pady=(100, 5)
        )

        tk.Label(
            painel_direito,
            text="Entre para acessar o sistema",
            bg=self.BRANCO,
            fg=self.CINZA_TEXTO,
            font=("Arial", 11)
        ).pack(
            pady=(0, 25)
        )

        frame = tk.Frame(
            painel_direito,
            bg=self.BRANCO
        )

        frame.pack()

        # LOGIN

        tk.Label(
            frame,
            text="Login",
            bg=self.BRANCO,
            fg=self.CINZA_TEXTO,
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=(10, 5)
        )

        self.entrada_login = tk.Entry(
            frame,
            width=32,
            font=("Arial", 11),
            relief="solid",
            bd=1
        )

        self.entrada_login.grid(
            row=1,
            column=0,
            ipady=8
        )

        # SENHA

        tk.Label(
            frame,
            text="Senha",
            bg=self.BRANCO,
            fg=self.CINZA_TEXTO,
            font=("Arial", 10, "bold")
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=(15, 5)
        )

        self.entrada_senha = tk.Entry(
            frame,
            width=32,
            font=("Arial", 11),
            show="*",
            relief="solid",
            bd=1
        )

        self.entrada_senha.grid(
            row=3,
            column=0,
            ipady=8
        )

        # ENTRAR

        self.criar_botao(
            painel_direito,
            "ENTRAR",
            self.fazer_login,
            28
        ).pack(
            pady=(25, 10)
        )

        # CADASTRO

        botao_cadastro = tk.Button(
            painel_direito,
            text="Criar novo usuário",
            command=self.tela_cadastro,
            bg=self.BRANCO,
            fg=self.AZUL,
            activebackground=self.BRANCO,
            activeforeground=self.AZUL_ESCURO,
            relief="flat",
            cursor="hand2",
            font=("Arial", 10, "bold")
        )

        botao_cadastro.pack()

    # ==================================================
    # LOGIN
    # ==================================================

    def fazer_login(self):

        login = self.entrada_login.get().strip()
        senha = self.entrada_senha.get().strip()

        if not login or not senha:

            messagebox.showwarning(
                "Atenção",
                "Preencha o login e a senha."
            )

            return

        for usuario in self.usuarios:

            if (
                usuario.login_usuario == login
                and usuario.senha == senha
            ):

                usuario.login(
                    login,
                    senha
                )

                self.usuario_logado = usuario

                if isinstance(
                    usuario,
                    Coordenador
                ):

                    self.tela_coordenador()

                else:

                    self.tela_professor()

                return

        messagebox.showerror(
            "Login",
            "Login ou senha incorretos."
        )

    # ==================================================
    # CADASTRO DE USUÁRIO
    # ==================================================

    def tela_cadastro(self):

        self.limpar_tela()

        frame = tk.Frame(
            self.root,
            bg=self.CINZA
        )

        frame.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            frame,
            text="CRIAR CONTA",
            bg=self.CINZA,
            fg=self.AZUL_ESCURO,
            font=("Arial", 25, "bold")
        ).pack(
            pady=(50, 5)
        )

        tk.Label(
            frame,
            text="Preencha os dados abaixo",
            bg=self.CINZA,
            fg=self.CINZA_TEXTO,
            font=("Arial", 11)
        ).pack(
            pady=(0, 20)
        )

        formulario = tk.Frame(
            frame,
            bg=self.BRANCO,
            padx=40,
            pady=25
        )

        formulario.pack()

        # Campos

        campos = []

        textos = [
            "Nome",
            "Login",
            "Senha"
        ]

        for i, texto in enumerate(textos):

            tk.Label(
                formulario,
                text=texto,
                bg=self.BRANCO,
                fg=self.CINZA_TEXTO,
                font=("Arial", 10, "bold")
            ).grid(
                row=i,
                column=0,
                sticky="w",
                pady=5
            )

            entrada = tk.Entry(
                formulario,
                width=32,
                show="*" if texto == "Senha" else "",
                relief="solid",
                bd=1
            )

            entrada.grid(
                row=i,
                column=1,
                padx=15,
                ipady=5
            )

            campos.append(
                entrada
            )

        entrada_nome = campos[0]
        entrada_login = campos[1]
        entrada_senha = campos[2]

        # TIPO

        tk.Label(
            formulario,
            text="Tipo",
            bg=self.BRANCO,
            fg=self.CINZA_TEXTO,
            font=("Arial", 10, "bold")
        ).grid(
            row=3,
            column=0,
            sticky="w",
            pady=10
        )

        tipo = tk.StringVar(
            value="Professor"
        )

        tk.OptionMenu(
            formulario,
            tipo,
            "Professor",
            "Coordenador"
        ).grid(
            row=3,
            column=1,
            sticky="w"
        )

        self.criar_botao(
            frame,
            "CADASTRAR",
            lambda: self.cadastrar_usuario(
                entrada_nome,
                entrada_login,
                entrada_senha,
                tipo
            ),
            25
        ).pack(
            pady=20
        )

        tk.Button(
            frame,
            text="Voltar para o login",
            command=self.tela_login,
            bg=self.CINZA,
            fg=self.AZUL,
            relief="flat",
            cursor="hand2",
            font=("Arial", 10, "bold")
        ).pack()

    # ==================================================
    # CADASTRAR USUÁRIO
    # ==================================================

    def cadastrar_usuario(
        self,
        entrada_nome,
        entrada_login,
        entrada_senha,
        tipo
    ):

        nome = entrada_nome.get().strip()
        login = entrada_login.get().strip()
        senha = entrada_senha.get().strip()

        if (
            not nome
            or not login
            or not senha
        ):

            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos."
            )

            return

        for usuario in self.usuarios:

            if usuario.login_usuario == login:

                messagebox.showerror(
                    "Erro",
                    "Esse login já está cadastrado."
                )

                return

        if tipo.get() == "Professor":

            novo_usuario = Professor(
                nome,
                login,
                senha
            )

        else:

            novo_usuario = Coordenador(
                nome,
                login,
                senha
            )

        self.usuarios.append(
            novo_usuario
        )

        novo_usuario.cadastrar()

        self.salvar_dados()

        messagebox.showinfo(
            "Sucesso",
            "Usuário cadastrado com sucesso!"
        )

        self.tela_login()

    # ==================================================
    # CABEÇALHO
    # ==================================================

    def criar_cabecalho(
        self,
        titulo,
        subtitulo
    ):

        header = tk.Frame(
            self.root,
            bg=self.AZUL_ESCURO,
            height=100
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(
            False
        )

        tk.Label(
            header,
            text=titulo,
            bg=self.AZUL_ESCURO,
            fg=self.BRANCO,
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=35,
            pady=(20, 0)
        )

        tk.Label(
            header,
            text=subtitulo,
            bg=self.AZUL_ESCURO,
            fg="#D9EAF7",
            font=("Arial", 10)
        ).pack(
            anchor="w",
            padx=35
        )

    # ==================================================
    # MENU COORDENADOR
    # ==================================================

    def tela_coordenador(self):

        self.limpar_tela()

        self.criar_cabecalho(
            "Painel do Coordenador",
            f"Usuário: {self.usuario_logado.nome}"
        )

        conteudo = tk.Frame(
            self.root,
            bg=self.CINZA
        )

        conteudo.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            conteudo,
            text="Gerenciamento",
            bg=self.CINZA,
            fg=self.AZUL_ESCURO,
            font=("Arial", 18, "bold")
        ).pack(
            pady=(30, 20)
        )

        frame = tk.Frame(
            conteudo,
            bg=self.CINZA
        )

        frame.pack()

        botoes = [
            ("Cadastrar Sala", self.cadastrar_sala),
            ("Consultar Salas", self.consultar_salas),
            ("Alterar Sala", self.alterar_sala),
            ("Excluir Sala", self.excluir_sala),
            ("Cadastrar Turma", self.cadastrar_turma),
            ("Consultar Turmas", self.consultar_turmas),
            ("Alterar Turma", self.alterar_turma),
            ("Excluir Turma", self.excluir_turma)
        ]

        for i, (
            texto,
            comando
        ) in enumerate(botoes):

            linha = i // 2
            coluna = i % 2

            self.criar_botao(
                frame,
                texto,
                comando,
                25
            ).grid(
                row=linha,
                column=coluna,
                padx=10,
                pady=8
            )

        self.criar_botao(
            conteudo,
            "SAIR",
            self.logout,
            25,
            self.VERMELHO
        ).pack(
            pady=25
        )

    # ==================================================
    # MENU PROFESSOR
    # ==================================================

    def tela_professor(self):

        self.limpar_tela()

        self.criar_cabecalho(
            "Painel do Professor",
            f"Usuário: {self.usuario_logado.nome}"
        )

        conteudo = tk.Frame(
            self.root,
            bg=self.CINZA
        )

        conteudo.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            conteudo,
            text="Área Acadêmica",
            bg=self.CINZA,
            fg=self.AZUL_ESCURO,
            font=("Arial", 18, "bold")
        ).pack(
            pady=(40, 25)
        )

        frame = tk.Frame(
            conteudo,
            bg=self.CINZA
        )

        frame.pack()

        botoes = [
            ("Consultar Salas", self.consultar_salas),
            ("Solicitar Reserva", self.solicitar_reserva),
            ("Consultar Reservas", self.consultar_reservas),
            ("Alterar Reserva", self.alterar_reserva),
            ("Cancelar Reserva", self.cancelar_reserva)
        ]

        for i, (
            texto,
            comando
        ) in enumerate(botoes):

            linha = i // 2
            coluna = i % 2

            self.criar_botao(
                frame,
                texto,
                comando,
                25
            ).grid(
                row=linha,
                column=coluna,
                padx=10,
                pady=8
            )

        self.criar_botao(
            conteudo,
            "SAIR",
            self.logout,
            25,
            self.VERMELHO
        ).pack(
            pady=30
        )

    # ==================================================
    # CADASTRAR SALA
    # ==================================================

    def cadastrar_sala(self):

        janela = tk.Toplevel(
            self.root
        )

        janela.title(
            "Cadastrar Sala"
        )

        janela.geometry(
            "450x330"
        )

        janela.configure(
            bg=self.CINZA
        )

        tk.Label(
            janela,
            text="Cadastrar Sala",
            bg=self.CINZA,
            fg=self.AZUL_ESCURO,
            font=("Arial", 20, "bold")
        ).pack(
            pady=25
        )

        frame = tk.Frame(
            janela,
            bg=self.BRANCO,
            padx=30,
            pady=20
        )

        frame.pack()

        tk.Label(
            frame,
            text="Número da sala:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        entrada_numero = tk.Entry(
            frame,
            width=25
        )

        entrada_numero.grid(
            row=0,
            column=1
        )

        tk.Label(
            frame,
            text="Capacidade:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        entrada_capacidade = tk.Entry(
            frame,
            width=25
        )

        entrada_capacidade.grid(
            row=1,
            column=1
        )

        def cadastrar():

            numero = entrada_numero.get().strip()
            capacidade = entrada_capacidade.get().strip()

            if not numero or not capacidade:

                messagebox.showwarning(
                    "Atenção",
                    "Preencha todos os campos.",
                    parent=janela
                )

                return

            try:

                capacidade = int(
                    capacidade
                )

                if capacidade <= 0:

                    raise ValueError

            except ValueError:

                messagebox.showerror(
                    "Erro",
                    "Digite uma capacidade válida.",
                    parent=janela
                )

                return

            for sala in self.salas:

                if sala.numero == numero:

                    messagebox.showerror(
                        "Erro",
                        "Essa sala já existe.",
                        parent=janela
                    )

                    return

            sala = Sala(
                numero,
                capacidade
            )

            self.salas.append(
                sala
            )

            self.usuario_logado.cadastrarSala(
                sala
            )

            self.salvar_dados()

            messagebox.showinfo(
                "Sucesso",
                "Sala cadastrada com sucesso!",
                parent=janela
            )

            janela.destroy()

        self.criar_botao(
            janela,
            "CADASTRAR",
            cadastrar,
            22
        ).pack(
            pady=20
        )

    # ==================================================
    # CONSULTAR SALAS
    # ==================================================

    def consultar_salas(self):

        janela = tk.Toplevel(
            self.root
        )

        janela.title(
            "Consultar Salas"
        )

        janela.geometry(
            "700x500"
        )

        janela.configure(
            bg=self.CINZA
        )

        tk.Label(
            janela,
            text="Salas Cadastradas",
            bg=self.CINZA,
            fg=self.AZUL_ESCURO,
            font=("Arial", 20, "bold")
        ).pack(
            pady=25
        )

        if not self.salas:

            tk.Label(
                janela,
                text="Nenhuma sala cadastrada.",
                bg=self.CINZA,
                fg=self.CINZA_TEXTO,
                font=("Arial", 12)
            ).pack()

            return

        tabela = tk.Frame(
            janela,
            bg=self.BRANCO,
            padx=15,
            pady=15
        )

        tabela.pack()

        cabecalhos = [
            "Sala",
            "Capacidade",
            "Status"
        ]

        for coluna, texto in enumerate(
            cabecalhos
        ):

            tk.Label(
                tabela,
                text=texto,
                width=20,
                bg=self.AZUL,
                fg=self.BRANCO,
                font=("Arial", 10, "bold")
            ).grid(
                row=0,
                column=coluna,
                padx=1,
                pady=1
            )

        for linha, sala in enumerate(
            self.salas,
            start=1
        ):

            status = (
                "Disponível"
                if sala.disponivel
                else "Indisponível"
            )

            valores = [
                sala.numero,
                sala.capacidade,
                status
            ]

            for coluna, valor in enumerate(
                valores
            ):

                tk.Label(
                    tabela,
                    text=valor,
                    width=20,
                    bg=self.BRANCO,
                    fg=(
                        self.VERDE
                        if status == "Disponível"
                        else self.VERMELHO
                    )
                    if coluna == 2
                    else self.CINZA_TEXTO
                ).grid(
                    row=linha,
                    column=coluna,
                    padx=1,
                    pady=5
                )

    # ==================================================
    # ALTERAR SALA
    # ==================================================

    def alterar_sala(self):

        if not self.salas:

            messagebox.showinfo(
                "Aviso",
                "Nenhuma sala cadastrada."
            )

            return

        janela = tk.Toplevel(
            self.root
        )

        janela.title(
            "Alterar Sala"
        )

        janela.geometry(
            "450x330"
        )

        janela.configure(
            bg=self.CINZA
        )

        tk.Label(
            janela,
            text="Alterar Sala",
            bg=self.CINZA,
            fg=self.AZUL_ESCURO,
            font=("Arial", 20, "bold")
        ).pack(
            pady=25
        )

        frame = tk.Frame(
            janela,
            bg=self.BRANCO,
            padx=30,
            pady=20
        )

        frame.pack()

        tk.Label(
            frame,
            text="Número da sala:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        entrada_numero = tk.Entry(
            frame,
            width=25
        )

        entrada_numero.grid(
            row=0,
            column=1
        )

        tk.Label(
            frame,
            text="Nova capacidade:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        entrada_capacidade = tk.Entry(
            frame,
            width=25
        )

        entrada_capacidade.grid(
            row=1,
            column=1
        )

        def alterar():

            numero = entrada_numero.get().strip()

            try:

                capacidade = int(
                    entrada_capacidade.get()
                )

            except ValueError:

                messagebox.showerror(
                    "Erro",
                    "Digite uma capacidade válida.",
                    parent=janela
                )

                return

            for sala in self.salas:

                if sala.numero == numero:

                    self.usuario_logado.alterarSala(
                        sala,
                        capacidade
                    )

                    self.salvar_dados()

                    messagebox.showinfo(
                        "Sucesso",
                        "Sala alterada com sucesso!",
                        parent=janela
                    )

                    janela.destroy()

                    return

            messagebox.showerror(
                "Erro",
                "Sala não encontrada.",
                parent=janela
            )

        self.criar_botao(
            janela,
            "SALVAR ALTERAÇÕES",
            alterar,
            22
        ).pack(
            pady=20
        )

    # ==================================================
    # EXCLUIR SALA
    # ==================================================

    def excluir_sala(self):

        if not self.salas:

            messagebox.showinfo(
                "Aviso",
                "Nenhuma sala cadastrada."
            )

            return

        janela = tk.Toplevel(
            self.root
        )

        janela.title(
            "Excluir Sala"
        )

        janela.geometry(
            "450x300"
        )

        janela.configure(
            bg=self.CINZA
        )

        tk.Label(
            janela,
            text="Excluir Sala",
            bg=self.CINZA,
            fg=self.AZUL_ESCURO,
            font=("Arial", 20, "bold")
        ).pack(
            pady=25
        )

        tk.Label(
            janela,
            text="Número da sala:",
            bg=self.CINZA
        ).pack()

        entrada = tk.Entry(
            janela,
            width=30
        )

        entrada.pack(
            pady=10
        )

        def excluir():

            numero = entrada.get().strip()

            for sala in self.salas:

                if sala.numero == numero:

                    if not sala.disponivel:

                        messagebox.showwarning(
                            "Atenção",
                            "A sala possui uma reserva ativa.",
                            parent=janela
                        )

                        return

                    confirmar = messagebox.askyesno(
                        "Confirmar",
                        f"Excluir a sala {numero}?",
                        parent=janela
                    )

                    if confirmar:

                        self.usuario_logado.excluirSala(
                            sala
                        )

                        self.salas.remove(
                            sala
                        )

                        self.salvar_dados()

                        messagebox.showinfo(
                            "Sucesso",
                            "Sala excluída.",
                            parent=janela
                        )

                        janela.destroy()

                    return

            messagebox.showerror(
                "Erro",
                "Sala não encontrada.",
                parent=janela
            )

        self.criar_botao(
            janela,
            "EXCLUIR",
            excluir,
            20,
            self.VERMELHO
        ).pack(
            pady=20
        )

    # ==================================================
    # CADASTRAR TURMA
    # ==================================================

    def cadastrar_turma(self):

        janela = tk.Toplevel(
            self.root
        )

        janela.title(
            "Cadastrar Turma"
        )

        janela.geometry(
            "500x380"
        )

        janela.configure(
            bg=self.CINZA
        )

        tk.Label(
            janela,
            text="Cadastrar Turma",
            bg=self.CINZA,
            fg=self.AZUL_ESCURO,
            font=("Arial", 20, "bold")
        ).pack(
            pady=25
        )

        frame = tk.Frame(
            janela,
            bg=self.BRANCO,
            padx=30,
            pady=20
        )

        frame.pack()

        campos = [
            ("Nome da turma:", 0),
            ("Curso:", 1),
            ("Quantidade de alunos:", 2)
        ]

        entradas = []

        for texto, linha in campos:

            tk.Label(
                frame,
                text=texto
            ).grid(
                row=linha,
                column=0,
                padx=10,
                pady=10
            )

            entrada = tk.Entry(
                frame,
                width=28
            )

            entrada.grid(
                row=linha,
                column=1
            )

            entradas.append(
                entrada
            )

        def cadastrar():

            nome = entradas[0].get().strip()
            curso = entradas[1].get().strip()
            alunos = entradas[2].get().strip()

            if not nome or not curso or not alunos:

                messagebox.showwarning(
                    "Atenção",
                    "Preencha todos os campos.",
                    parent=janela
                )

                return

            try:

                alunos = int(alunos)

                if alunos <= 0:
                    raise ValueError

            except ValueError:

                messagebox.showerror(
                    "Erro",
                    "Quantidade de alunos inválida.",
                    parent=janela
                )

                return

            for turma in self.turmas:

                if turma.nome == nome:

                    messagebox.showerror(
                        "Erro",
                        "Essa turma já existe.",
                        parent=janela
                    )

                    return

            turma = Turma(
                nome,
                curso,
                alunos
            )

            self.turmas.append(
                turma
            )

            turma.cadastrar()

            self.salvar_dados()

            messagebox.showinfo(
                "Sucesso",
                "Turma cadastrada com sucesso!",
                parent=janela
            )

            janela.destroy()

        self.criar_botao(
            janela,
            "CADASTRAR",
            cadastrar,
            22
        ).pack(
            pady=20
        )

    # ==================================================
    # CONSULTAR TURMAS
    # ==================================================

    def consultar_turmas(self):

        janela = tk.Toplevel(
            self.root
        )

        janela.title(
            "Consultar Turmas"
        )

        janela.geometry(
            "750x500"
        )

        janela.configure(
            bg=self.CINZA
        )

        tk.Label(
            janela,
            text="Turmas Cadastradas",
            bg=self.CINZA,
            fg=self.AZUL_ESCURO,
            font=("Arial", 20, "bold")
        ).pack(
            pady=25
        )

        if not self.turmas:

            tk.Label(
                janela,
                text="Nenhuma turma cadastrada.",
                bg=self.CINZA,
                fg=self.CINZA_TEXTO
            ).pack()

            return

        tabela = tk.Frame(
            janela,
            bg=self.BRANCO,
            padx=15,
            pady=15
        )

        tabela.pack()

        cabecalhos = [
            "Turma",
            "Curso",
            "Alunos"
        ]

        for coluna, texto in enumerate(
            cabecalhos
        ):

            tk.Label(
                tabela,
                text=texto,
                width=23,
                bg=self.AZUL,
                fg=self.BRANCO,
                font=("Arial", 10, "bold")
            ).grid(
                row=0,
                column=coluna,
                padx=1
            )

        for linha, turma in enumerate(
            self.turmas,
            start=1
        ):

            valores = [
                turma.nome,
                turma.curso,
                turma.quantidade_alunos
            ]

            for coluna, valor in enumerate(
                valores
            ):

                tk.Label(
                    tabela,
                    text=valor,
                    width=23,
                    bg=self.BRANCO,
                    fg=self.CINZA_TEXTO
                ).grid(
                    row=linha,
                    column=coluna,
                    pady=5
                )

    # ==================================================
    # ALTERAR TURMA
    # ==================================================

    def alterar_turma(self):

        if not self.turmas:

            messagebox.showinfo(
                "Aviso",
                "Nenhuma turma cadastrada."
            )

            return

        janela = tk.Toplevel(
            self.root
        )

        janela.title(
            "Alterar Turma"
        )

        janela.geometry(
            "500x380"
        )

        janela.configure(
            bg=self.CINZA
        )

        tk.Label(
            janela,
            text="Alterar Turma",
            bg=self.CINZA,
            fg=self.AZUL_ESCURO,
            font=("Arial", 20, "bold")
        ).pack(
            pady=25
        )

        frame = tk.Frame(
            janela,
            bg=self.BRANCO,
            padx=30,
            pady=20
        )

        frame.pack()

        labels = [
            "Nome da turma:",
            "Novo curso:",
            "Quantidade de alunos:"
        ]

        entradas = []

        for i, texto in enumerate(labels):

            tk.Label(
                frame,
                text=texto
            ).grid(
                row=i,
                column=0,
                padx=10,
                pady=10
            )

            entrada = tk.Entry(
                frame,
                width=28
            )

            entrada.grid(
                row=i,
                column=1
            )

            entradas.append(
                entrada
            )

        def alterar():

            nome = entradas[0].get().strip()
            curso = entradas[1].get().strip()

            try:

                alunos = int(
                    entradas[2].get()
                )

            except ValueError:

                messagebox.showerror(
                    "Erro",
                    "Quantidade inválida.",
                    parent=janela
                )

                return

            for turma in self.turmas:

                if turma.nome == nome:

                    turma.alterar(
                        curso,
                        alunos
                    )

                    self.salvar_dados()

                    messagebox.showinfo(
                        "Sucesso",
                        "Turma alterada com sucesso!",
                        parent=janela
                    )

                    janela.destroy()

                    return

            messagebox.showerror(
                "Erro",
                "Turma não encontrada.",
                parent=janela
            )

        self.criar_botao(
            janela,
            "SALVAR ALTERAÇÕES",
            alterar,
            22
        ).pack(
            pady=20
        )

    # ==================================================
    # EXCLUIR TURMA
    # ==================================================

    def excluir_turma(self):

        if not self.turmas:

            messagebox.showinfo(
                "Aviso",
                "Nenhuma turma cadastrada."
            )

            return

        janela = tk.Toplevel(
            self.root
        )

        janela.title(
            "Excluir Turma"
        )

        janela.geometry(
            "450x300"
        )

        janela.configure(
            bg=self.CINZA
        )

        tk.Label(
            janela,
            text="Excluir Turma",
            bg=self.CINZA,
            fg=self.AZUL_ESCURO,
            font=("Arial", 20, "bold")
        ).pack(
            pady=25
        )

        tk.Label(
            janela,
            text="Nome da turma:",
            bg=self.CINZA
        ).pack()

        entrada = tk.Entry(
            janela,
            width=30
        )

        entrada.pack(
            pady=10
        )

        def excluir():

            nome = entrada.get().strip()

            for turma in self.turmas:

                if turma.nome == nome:

                    confirmar = messagebox.askyesno(
                        "Confirmar",
                        f"Excluir a turma {nome}?",
                        parent=janela
                    )

                    if confirmar:

                        turma.excluir()

                        self.turmas.remove(
                            turma
                        )

                        self.salvar_dados()

                        messagebox.showinfo(
                            "Sucesso",
                            "Turma excluída.",
                            parent=janela
                        )

                        janela.destroy()

                    return

            messagebox.showerror(
                "Erro",
                "Turma não encontrada.",
                parent=janela
            )

        self.criar_botao(
            janela,
            "EXCLUIR",
            excluir,
            20,
            self.VERMELHO
        ).pack(
            pady=20
        )

    # ==================================================
    # SOLICITAR RESERVA
    # ==================================================

    def solicitar_reserva(self):

        if not self.salas:

            messagebox.showinfo(
                "Aviso",
                "Nenhuma sala cadastrada."
            )

            return

        if not self.turmas:

            messagebox.showinfo(
                "Aviso",
                "Nenhuma turma cadastrada."
            )

            return

        salas_disponiveis = [
            sala
            for sala in self.salas
            if sala.disponivel
        ]

        if not salas_disponiveis:

            messagebox.showinfo(
                "Aviso",
                "Não existem salas disponíveis."
            )

            return

        janela = tk.Toplevel(
            self.root
        )

        janela.title(
            "Solicitar Reserva"
        )

        janela.geometry(
            "500x500"
        )

        janela.configure(
            bg=self.CINZA
        )

        tk.Label(
            janela,
            text="Solicitar Reserva",
            bg=self.CINZA,
            fg=self.AZUL_ESCURO,
            font=("Arial", 20, "bold")
        ).pack(
            pady=25
        )

        frame = tk.Frame(
            janela,
            bg=self.BRANCO,
            padx=30,
            pady=20
        )

        frame.pack()

        # SALA

        tk.Label(
            frame,
            text="Sala:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        salas_nomes = [
            sala.numero
            for sala in salas_disponiveis
        ]

        sala_var = tk.StringVar(
            value=salas_nomes[0]
        )

        tk.OptionMenu(
            frame,
            sala_var,
            *salas_nomes
        ).grid(
            row=0,
            column=1
        )

        # TURMA

        tk.Label(
            frame,
            text="Turma:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        turmas_nomes = [
            turma.nome
            for turma in self.turmas
        ]

        turma_var = tk.StringVar(
            value=turmas_nomes[0]
        )

        tk.OptionMenu(
            frame,
            turma_var,
            *turmas_nomes
        ).grid(
            row=1,
            column=1
        )

        # DATA

        tk.Label(
            frame,
            text="Data:"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=10
        )

        entrada_data = tk.Entry(
            frame,
            width=25
        )

        entrada_data.grid(
            row=2,
            column=1
        )

        # HORÁRIO

        tk.Label(
            frame,
            text="Horário:"
        ).grid(
            row=3,
            column=0,
            padx=10,
            pady=10
        )

        entrada_horario = tk.Entry(
            frame,
            width=25
        )

        entrada_horario.grid(
            row=3,
            column=1
        )

        def reservar():

            data = entrada_data.get().strip()
            horario = entrada_horario.get().strip()

            if not data or not horario:

                messagebox.showwarning(
                    "Atenção",
                    "Informe data e horário.",
                    parent=janela
                )

                return

            sala_escolhida = None

            for sala in self.salas:

                if sala.numero == sala_var.get():

                    sala_escolhida = sala
                    break

            turma_escolhida = None

            for turma in self.turmas:

                if turma.nome == turma_var.get():

                    turma_escolhida = turma
                    break

            reserva = Reserva(
                self.usuario_logado,
                sala_escolhida,
                turma_escolhida,
                data,
                horario
            )

            self.usuario_logado.solicitarReserva(
                reserva
            )

            if reserva.status == "Ativa":

                self.reservas.append(
                    reserva
                )

                self.salvar_dados()

                messagebox.showinfo(
                    "Sucesso",
                    "Reserva realizada com sucesso!",
                    parent=janela
                )

                janela.destroy()

        self.criar_botao(
            janela,
            "SOLICITAR RESERVA",
            reservar,
            25
        ).pack(
            pady=25
        )

    # ==================================================
    # CONSULTAR RESERVAS
    # ==================================================

    def consultar_reservas(self):

        janela = tk.Toplevel(
            self.root
        )

        janela.title(
            "Consultar Reservas"
        )

        janela.geometry(
            "800x500"
        )

        janela.configure(
            bg=self.CINZA
        )

        tk.Label(
            janela,
            text="Minhas Reservas",
            bg=self.CINZA,
            fg=self.AZUL_ESCURO,
            font=("Arial", 20, "bold")
        ).pack(
            pady=25
        )

        minhas_reservas = [
            reserva
            for reserva in self.reservas
            if reserva.professor == self.usuario_logado
        ]

        if not minhas_reservas:

            tk.Label(
                janela,
                text="Você não possui reservas.",
                bg=self.CINZA,
                fg=self.CINZA_TEXTO
            ).pack()

            return

        tabela = tk.Frame(
            janela,
            bg=self.BRANCO,
            padx=10,
            pady=10
        )

        tabela.pack()

        cabecalhos = [
            "Sala",
            "Turma",
            "Data",
            "Horário",
            "Status"
        ]

        for coluna, texto in enumerate(
            cabecalhos
        ):

            tk.Label(
                tabela,
                text=texto,
                width=14,
                bg=self.AZUL,
                fg=self.BRANCO,
                font=("Arial", 10, "bold")
            ).grid(
                row=0,
                column=coluna,
                padx=1
            )

        for linha, reserva in enumerate(
            minhas_reservas,
            start=1
        ):

            valores = [
                reserva.sala.numero,
                reserva.turma.nome,
                reserva.data,
                reserva.horario,
                reserva.status
            ]

            for coluna, valor in enumerate(
                valores
            ):

                tk.Label(
                    tabela,
                    text=valor,
                    width=14,
                    bg=self.BRANCO,
                    fg=(
                        self.VERDE
                        if reserva.status == "Ativa"
                        else self.VERMELHO
                    )
                    if coluna == 4
                    else self.CINZA_TEXTO
                ).grid(
                    row=linha,
                    column=coluna,
                    pady=5
                )

    # ==================================================
    # ALTERAR RESERVA
    # ==================================================

    def alterar_reserva(self):

        minhas_reservas = [
            reserva
            for reserva in self.reservas
            if (
                reserva.professor == self.usuario_logado
                and reserva.status == "Ativa"
            )
        ]

        if not minhas_reservas:

            messagebox.showinfo(
                "Aviso",
                "Você não possui reservas ativas."
            )

            return

        janela = tk.Toplevel(
            self.root
        )

        janela.title(
            "Alterar Reserva"
        )

        janela.geometry(
            "500x400"
        )

        janela.configure(
            bg=self.CINZA
        )

        tk.Label(
            janela,
            text="Alterar Reserva",
            bg=self.CINZA,
            fg=self.AZUL_ESCURO,
            font=("Arial", 20, "bold")
        ).pack(
            pady=25
        )

        opcoes = []

        for i, reserva in enumerate(
            minhas_reservas
        ):

            opcoes.append(
                f"Sala {reserva.sala.numero} | "
                f"{reserva.data} | "
                f"{reserva.horario}"
            )

        reserva_var = tk.StringVar(
            value=opcoes[0]
        )

        tk.OptionMenu(
            janela,
            reserva_var,
            *opcoes
        ).pack(
            pady=10
        )

        tk.Label(
            janela,
            text="Nova data:",
            bg=self.CINZA
        ).pack()

        entrada_data = tk.Entry(
            janela,
            width=30
        )

        entrada_data.pack(
            pady=8
        )

        tk.Label(
            janela,
            text="Novo horário:",
            bg=self.CINZA
        ).pack()

        entrada_horario = tk.Entry(
            janela,
            width=30
        )

        entrada_horario.pack(
            pady=8
        )

        def alterar():

            indice = opcoes.index(
                reserva_var.get()
            )

            reserva = minhas_reservas[
                indice
            ]

            data = entrada_data.get().strip()
            horario = entrada_horario.get().strip()

            if not data or not horario:

                messagebox.showwarning(
                    "Atenção",
                    "Preencha todos os campos.",
                    parent=janela
                )

                return

            reserva.alterarReserva(
                data,
                horario
            )

            self.salvar_dados()

            messagebox.showinfo(
                "Sucesso",
                "Reserva alterada com sucesso!",
                parent=janela
            )

            janela.destroy()

        self.criar_botao(
            janela,
            "SALVAR ALTERAÇÕES",
            alterar,
            25
        ).pack(
            pady=25
        )

    # ==================================================
    # CANCELAR RESERVA
    # ==================================================

    def cancelar_reserva(self):

        minhas_reservas = [
            reserva
            for reserva in self.reservas
            if (
                reserva.professor == self.usuario_logado
                and reserva.status == "Ativa"
            )
        ]

        if not minhas_reservas:

            messagebox.showinfo(
                "Aviso",
                "Você não possui reservas ativas."
            )

            return

        janela = tk.Toplevel(
            self.root
        )

        janela.title(
            "Cancelar Reserva"
        )

        janela.geometry(
            "500x350"
        )

        janela.configure(
            bg=self.CINZA
        )

        tk.Label(
            janela,
            text="Cancelar Reserva",
            bg=self.CINZA,
            fg=self.VERMELHO,
            font=("Arial", 20, "bold")
        ).pack(
            pady=30
        )

        opcoes = []

        for reserva in minhas_reservas:

            opcoes.append(
                f"Sala {reserva.sala.numero} | "
                f"{reserva.data} | "
                f"{reserva.horario}"
            )

        reserva_var = tk.StringVar(
            value=opcoes[0]
        )

        tk.OptionMenu(
            janela,
            reserva_var,
            *opcoes
        ).pack(
            pady=15
        )

        def cancelar():

            indice = opcoes.index(
                reserva_var.get()
            )

            reserva = minhas_reservas[
                indice
            ]

            confirmar = messagebox.askyesno(
                "Confirmar",
                "Deseja cancelar esta reserva?",
                parent=janela
            )

            if not confirmar:
                return

            reserva.cancelarReserva()

            self.salvar_dados()

            messagebox.showinfo(
                "Sucesso",
                "Reserva cancelada.",
                parent=janela
            )

            janela.destroy()

        self.criar_botao(
            janela,
            "CANCELAR RESERVA",
            cancelar,
            25,
            self.VERMELHO
        ).pack(
            pady=20
        )

    # ==================================================
    # LOGOUT
    # ==================================================

    def logout(self):

        if self.usuario_logado:

            self.usuario_logado.logout()

        self.usuario_logado = None

        self.tela_login()