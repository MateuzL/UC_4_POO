from flask import Flask, render_template, request, redirect, url_for, session

from usuario import Usuario
from coordenador import Coordenador
from professor import Professor
from sala import Sala
from turma import Turma
from reserva import Reserva

app = Flask(__name__)

app.secret_key = "sistema-educacional"

usuarios = []
salas = []
turmas = []
reservas = []

arquivo_dados = "dados.txt"

# ==========================================================

# CARREGAR DADOS

# ==========================================================

def carregar_dados():


    usuarios.clear()
    salas.clear()
    turmas.clear()
    reservas.clear()

    try:

        with open(arquivo_dados, "r", encoding="utf-8") as arquivo:

            secao = None
            dados_reservas = []

            for linha in arquivo:

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

                if secao == "usuarios":

                    partes = linha.split("|")

                    if len(partes) >= 4:

                        nome = partes[0]
                        login = partes[1]
                        senha = partes[2]
                        tipo = partes[3]

                        if tipo == "Coordenador":

                            usuario = Coordenador(
                                nome,
                                login,
                                senha
                            )

                        elif tipo == "Professor":

                            usuario = Professor(
                                nome,
                                login,
                                senha
                            )

                        else:

                            usuario = Usuario(
                                nome,
                                login,
                                senha
                            )

                        usuarios.append(usuario)

                elif secao == "salas":

                    partes = linha.split("|")

                    if len(partes) >= 3:

                        numero = partes[0]
                        capacidade = int(partes[1])
                        disponivel = partes[2] == "1"

                        sala = Sala(
                            numero,
                            capacidade
                        )

                        sala.disponivel = disponivel

                        salas.append(sala)

                elif secao == "turmas":

                    partes = linha.split("|")

                    if len(partes) >= 3:

                        nome = partes[0]
                        curso = partes[1]
                        quantidade = int(partes[2])

                        turma = Turma(
                            nome,
                            curso,
                            quantidade
                        )

                        turmas.append(turma)

                elif secao == "reservas":

                    partes = linha.split("|")

                    if len(partes) >= 6:

                        dados_reservas.append(partes)

            # Reconstruir reservas

            for partes in dados_reservas:

                login_professor = partes[0]
                numero_sala = partes[1]
                nome_turma = partes[2]
                data = partes[3]
                horario = partes[4]
                status = partes[5]

                professor = None
                sala = None
                turma = None

                for usuario in usuarios:

                    if usuario.login_usuario == login_professor:

                        professor = usuario
                        break

                for item in salas:

                    if item.numero == numero_sala:

                        sala = item
                        break

                for item in turmas:

                    if item.nome == nome_turma:

                        turma = item
                        break

                if professor and sala and turma:

                    reserva = Reserva(
                        professor,
                        sala,
                        turma,
                        data,
                        horario
                    )

                    reserva.status = status

                    if status == "Ativa":

                        sala.disponivel = False

                    reservas.append(reserva)

    except FileNotFoundError:

        pass


# ==========================================================

# SALVAR DADOS

# ==========================================================

def salvar_dados():


    with open(
        arquivo_dados,
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write("=== USUARIOS ===\n")

        for usuario in usuarios:

            if isinstance(usuario, Coordenador):

                tipo = "Coordenador"

            elif isinstance(usuario, Professor):

                tipo = "Professor"

            else:

                tipo = "Usuario"

            arquivo.write(
                f"{usuario.nome}|"
                f"{usuario.login_usuario}|"
                f"{usuario.senha}|"
                f"{tipo}\n"
            )

        arquivo.write("\n=== SALAS ===\n")

        for sala in salas:

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

        arquivo.write("\n=== TURMAS ===\n")

        for turma in turmas:

            arquivo.write(
                f"{turma.nome}|"
                f"{turma.curso}|"
                f"{turma.quantidade_alunos}\n"
            )

        arquivo.write("\n=== RESERVAS ===\n")

        for reserva in reservas:

            arquivo.write(
                f"{reserva.professor.login_usuario}|"
                f"{reserva.sala.numero}|"
                f"{reserva.turma.nome}|"
                f"{reserva.data}|"
                f"{reserva.horario}|"
                f"{reserva.status}\n"
            )


# ==========================================================

# LOGIN

# ==========================================================

@app.route("/", methods=["GET", "POST"])
def login():


    mensagem = ""

    if request.method == "POST":

        login_usuario = request.form["login"].strip()
        senha = request.form["senha"].strip()

        usuario_encontrado = None

        for usuario in usuarios:

            if (
                usuario.login_usuario == login_usuario
                and usuario.senha == senha
            ):

                usuario_encontrado = usuario
                break

        if usuario_encontrado:

            usuario_encontrado.login(
                login_usuario,
                senha
            )

            session["login"] = (
                usuario_encontrado.login_usuario
            )

            if isinstance(
                usuario_encontrado,
                Coordenador
            ):

                return redirect(
                    url_for("coordenador")
                )

            elif isinstance(
                usuario_encontrado,
                Professor
            ):

                return redirect(
                    url_for("professor")
                )

        else:

            mensagem = "Login ou senha incorretos."

    return render_template(
        "login.html",
        mensagem=mensagem
    )


# ==========================================================

# LOGOUT

# ==========================================================

@app.route("/logout")
def logout():


    login_usuario = session.get("login")

    for usuario in usuarios:

        if usuario.login_usuario == login_usuario:

            usuario.logout()
            break

    session.clear()

    return redirect(
        url_for("login")
    )


# ==========================================================

# COORDENADOR

# ==========================================================

@app.route("/coordenador")
def coordenador():


    return render_template(
        "coordenador.html",
        salas=salas,
        turmas=turmas
    )


# ==========================================================

# CADASTRAR SALA

# ==========================================================

@app.route(
"/coordenador/sala/cadastrar",
methods=["GET", "POST"]
)
def cadastrar_sala():


    mensagem = ""

    if request.method == "POST":

        numero = request.form["numero"].strip()
        capacidade = request.form["capacidade"].strip()

        if not numero or not capacidade:

            mensagem = "Preencha todos os campos."

            return render_template(
                "cadastrar_sala.html",
                mensagem=mensagem
            )

        try:

            capacidade = int(capacidade)

            if capacidade <= 0:

                mensagem = (
                    "A capacidade deve ser maior que zero."
                )

                return render_template(
                    "cadastrar_sala.html",
                    mensagem=mensagem
                )

        except ValueError:

            mensagem = "Digite uma capacidade válida."

            return render_template(
                "cadastrar_sala.html",
                mensagem=mensagem
            )

        for sala in salas:

            if sala.numero == numero:

                mensagem = "Essa sala já existe."

                return render_template(
                    "cadastrar_sala.html",
                    mensagem=mensagem
                )

        sala = Sala(
            numero,
            capacidade
        )

        sala.cadastrar()

        salas.append(sala)

        salvar_dados()

        return redirect(
            url_for("coordenador")
        )

    return render_template(
        "cadastrar_sala.html",
        mensagem=mensagem
    )


# ==========================================================

# ALTERAR SALA

# ==========================================================

@app.route(
"/coordenador/sala/alterar/<numero>",
methods=["GET", "POST"]
)
def alterar_sala(numero):


    mensagem = ""

    sala_encontrada = None

    for sala in salas:

        if sala.numero == numero:

            sala_encontrada = sala
            break

    if sala_encontrada is None:

        return redirect(
            url_for("coordenador")
        )

    if request.method == "POST":

        capacidade = request.form[
            "capacidade"
        ].strip()

        try:

            capacidade = int(capacidade)

            if capacidade <= 0:

                mensagem = (
                    "A capacidade deve ser maior que zero."
                )

                return render_template(
                    "alterar_sala.html",
                    sala=sala_encontrada,
                    mensagem=mensagem
                )

        except ValueError:

            mensagem = "Digite uma capacidade válida."

            return render_template(
                "alterar_sala.html",
                sala=sala_encontrada,
                mensagem=mensagem
            )

        sala_encontrada.alterar(
            capacidade
        )

        salvar_dados()

        return redirect(
            url_for("coordenador")
        )

    return render_template(
        "alterar_sala.html",
        sala=sala_encontrada,
        mensagem=mensagem
    )


# ==========================================================

# EXCLUIR SALA

# ==========================================================

@app.route(
"/coordenador/sala/excluir/<numero>"
)
def excluir_sala(numero):


    sala_encontrada = None

    for sala in salas:

        if sala.numero == numero:

            sala_encontrada = sala
            break

    if sala_encontrada is None:

        return redirect(
            url_for("coordenador")
        )

    sala_encontrada.excluir()

    salas.remove(
        sala_encontrada
    )

    salvar_dados()

    return redirect(
        url_for("coordenador")
    )


# ==========================================================

# CADASTRAR TURMA

# ==========================================================

@app.route(
"/coordenador/turma/cadastrar",
methods=["GET", "POST"]
)
def cadastrar_turma():


    mensagem = ""

    if request.method == "POST":

        nome = request.form["nome"].strip()
        curso = request.form["curso"].strip()
        quantidade = request.form[
            "quantidade"
        ].strip()

        if not nome or not curso or not quantidade:

            mensagem = "Preencha todos os campos."

            return render_template(
                "cadastrar_turma.html",
                mensagem=mensagem
            )

        try:

            quantidade = int(quantidade)

            if quantidade <= 0:

                mensagem = (
                    "A quantidade deve ser maior que zero."
                )

                return render_template(
                    "cadastrar_turma.html",
                    mensagem=mensagem
                )

        except ValueError:

            mensagem = "Digite uma quantidade válida."

            return render_template(
                "cadastrar_turma.html",
                mensagem=mensagem
            )

        for turma in turmas:

            if turma.nome.lower() == nome.lower():

                mensagem = "Essa turma já existe."

                return render_template(
                    "cadastrar_turma.html",
                    mensagem=mensagem
                )

        turma = Turma(
            nome,
            curso,
            quantidade
        )

        turma.cadastrar()

        turmas.append(turma)

        salvar_dados()

        return redirect(
            url_for("consultar_turmas")
        )

    return render_template(
        "cadastrar_turma.html",
        mensagem=mensagem
    )


# ==========================================================

# CONSULTAR TURMAS

# ==========================================================

@app.route("/coordenador/turmas")
def consultar_turmas():


    return render_template(
        "turmas.html",
        turmas=turmas
    )


# ==========================================================

# ALTERAR TURMA

# ==========================================================

@app.route(
"/coordenador/turma/alterar/<nome>",
methods=["GET", "POST"]
)
def alterar_turma(nome):


    mensagem = ""

    turma_encontrada = None

    for turma in turmas:

        if turma.nome == nome:

            turma_encontrada = turma
            break

    if turma_encontrada is None:

        return redirect(
            url_for("consultar_turmas")
        )

    if request.method == "POST":

        curso = request.form["curso"].strip()

        quantidade = request.form[
            "quantidade"
        ].strip()

        if not curso or not quantidade:

            mensagem = "Preencha todos os campos."

            return render_template(
                "alterar_turma.html",
                turma=turma_encontrada,
                mensagem=mensagem
            )

        try:

            quantidade = int(quantidade)

            if quantidade <= 0:

                mensagem = (
                    "A quantidade deve ser maior que zero."
                )

                return render_template(
                    "alterar_turma.html",
                    turma=turma_encontrada,
                    mensagem=mensagem
                )

        except ValueError:

            mensagem = "Digite uma quantidade válida."

            return render_template(
                "alterar_turma.html",
                turma=turma_encontrada,
                mensagem=mensagem
            )

        turma_encontrada.alterar(
            curso,
            quantidade
        )

        salvar_dados()

        return redirect(
            url_for("consultar_turmas")
        )

    return render_template(
        "alterar_turma.html",
        turma=turma_encontrada,
        mensagem=mensagem
    )


# ==========================================================

# EXCLUIR TURMA

# ==========================================================

@app.route(
"/coordenador/turma/excluir/<nome>"
)
def excluir_turma(nome):


    turma_encontrada = None

    for turma in turmas:

        if turma.nome == nome:

            turma_encontrada = turma
            break

    if turma_encontrada is None:

        return redirect(
            url_for("consultar_turmas")
        )

    turma_encontrada.excluir()

    turmas.remove(
        turma_encontrada
    )

    salvar_dados()

    return redirect(
        url_for("consultar_turmas")
    )


# ==========================================================

# PROFESSOR

# ==========================================================

@app.route("/professor")
def professor():


    login_usuario = session.get("login")

    professor_logado = None

    for usuario in usuarios:

        if usuario.login_usuario == login_usuario:

            professor_logado = usuario
            break

    if professor_logado is None:

        return redirect(
            url_for("login")
        )

    return render_template(
        "professor.html",
        professor=professor_logado
    )


# ==========================================================

# CONSULTAR SALAS - PROFESSOR

# ==========================================================

@app.route("/professor/salas")
def professor_salas():


    return render_template(
        "professor_salas.html",
        salas=salas
    )


# ==========================================================

# CONSULTAR RESERVAS - PROFESSOR

# ==========================================================

@app.route("/professor/reservas")
def professor_reservas():


    reservas_professor = []

    login_usuario = session.get("login")

    for reserva in reservas:

        if (
            reserva.professor.login_usuario
            == login_usuario
        ):

            reservas_professor.append(
                reserva
            )

    return render_template(
        "professor_reservas.html",
        reservas=reservas_professor
    )


# ==========================================================

# SOLICITAR RESERVA

# ==========================================================

@app.route(
"/professor/reserva/cadastrar",
methods=["GET", "POST"]
)
def solicitar_reserva():


    mensagem = ""

    login_usuario = session.get("login")

    professor_logado = None

    for usuario in usuarios:

        if usuario.login_usuario == login_usuario:

            professor_logado = usuario
            break

    if professor_logado is None:

        return redirect(
            url_for("login")
        )

    if request.method == "POST":

        numero_sala = request.form["sala"]
        nome_turma = request.form["turma"]
        data = request.form["data"]
        horario = request.form["horario"]

        sala_encontrada = None
        turma_encontrada = None

        for sala in salas:

            if sala.numero == numero_sala:

                sala_encontrada = sala
                break

        for turma in turmas:

            if turma.nome == nome_turma:

                turma_encontrada = turma
                break

        if (
            sala_encontrada is None
            or turma_encontrada is None
        ):

            mensagem = "Sala ou turma inválida."

            return render_template(
                "cadastrar_reserva.html",
                salas=salas,
                turmas=turmas,
                mensagem=mensagem
            )

        if not sala_encontrada.consultarDisponibilidade():

            mensagem = "A sala não está disponível."

            return render_template(
                "cadastrar_reserva.html",
                salas=salas,
                turmas=turmas,
                mensagem=mensagem
            )

        reserva = Reserva(
            professor_logado,
            sala_encontrada,
            turma_encontrada,
            data,
            horario
        )

        reserva.criarReserva()

        reservas.append(reserva)

        salvar_dados()

        return redirect(
            url_for("professor_reservas")
        )

    return render_template(
        "cadastrar_reserva.html",
        salas=salas,
        turmas=turmas,
        mensagem=mensagem
    )


# ==========================================================

# ALTERAR RESERVA

# ==========================================================

@app.route(
"/professor/reserva/alterar/[int:indice](int:indice)",
methods=["GET", "POST"]
)
def alterar_reserva(indice):


    mensagem = ""

    login_usuario = session.get("login")

    reservas_professor = [
        reserva
        for reserva in reservas
        if reserva.professor.login_usuario
        == login_usuario
    ]

    if (
        indice < 0
        or indice >= len(reservas_professor)
    ):

        return redirect(
            url_for("professor_reservas")
        )

    reserva = reservas_professor[indice]

    if request.method == "POST":

        data = request.form["data"]
        horario = request.form["horario"]

        reserva.alterarReserva(
            data,
            horario
        )

        salvar_dados()

        return redirect(
            url_for("professor_reservas")
        )

    return render_template(
        "alterar_reserva.html",
        reserva=reserva,
        mensagem=mensagem
    )


# ==========================================================

# CANCELAR RESERVA

# ==========================================================

@app.route(
"/professor/reserva/cancelar/[int:indice](int:indice)"
)
def cancelar_reserva(indice):


    login_usuario = session.get("login")

    reservas_professor = [
        reserva
        for reserva in reservas
        if reserva.professor.login_usuario
        == login_usuario
    ]

    if (
        indice < 0
        or indice >= len(reservas_professor)
    ):

        return redirect(
            url_for("professor_reservas")
        )

    reserva = reservas_professor[indice]

    reserva.cancelarReserva()

    salvar_dados()

    return redirect(
        url_for("professor_reservas")
    )


# ==========================================================

# INICIALIZAÇÃO

# ==========================================================

carregar_dados()

if __name__ == "__main__":


    app.run(
        debug=True
    )

